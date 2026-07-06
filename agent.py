import os
import json  # Used for reading writing JSON
import chromadb # Vector database for the AI to get knowledge from (saved to harddrive)
import io  # Used to stream images purely in memory without hitting the hard drive
import asyncio #  Required to handle concurrent streaming loops efficiently
from google import genai #importants good SDK
from google.genai import types # Used to configure JSON
from PIL import Image, ImageGrab # Used to capture and open images
from google.adk import Agent # Google adk agent
from dotenv import load_dotenv # env files loader

load_dotenv() 

# Hardcoding a real key.
# .env already has gemini key, so we just require that instead.
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found. Make sure it's set in your .env file.")

# force the global GenAI Client initialization to target the alpha version pipeline
client = genai.Client(api_key=api_key, http_options={'api_version': 'v1alpha'})

# This background loop captures screenshots straight into RAM (BytesIO) 
# and feeds to the live socket web.
async def stream_roblox_screen(session):
    print("⚡ Optimized Screen streaming task active (Low-Latency RAM-to-WebSocket mode)...")
    while True:
        try:
            # Capture the screen directly 
            screenshot = ImageGrab.grab()
            
            # to reduce cpu load we downscale the images
            screenshot.thumbnail((768, 768))
            
            # Save the image into a temporarily in RAM instead of writing current_frame.jpg to your disk
            img_byte_arr = io.BytesIO()
            screenshot.save(img_byte_arr, format='JPEG', quality=30) # Dropped quality slightly to maximize throughput speed
            img_bytes = img_byte_arr.getvalue()

            # Push the resized image data frame directly to video channel
            await session.send_realtime_input(
                video=types.Blob(
                    data=img_bytes,
                    mime_type="image/jpeg"
                )
            )
        except Exception as e:
            print(f"Screen Stream Error: {str(e)}")

        # adding a delay so laptop doesnt fry.
        await asyncio.sleep(1.5)

#  background loop listens to incoming data from the agent
# and prints out the buddy's reactions cleanly.
async def receive_buddy_responses(session):
    async for response in session.receive():

        # The config tells Gemini it CAN call search_game_mechanics, but nothing
        # was ever listening for that tool_call, so Buddy would just go silent
        # whenever it tried to use the tool (it sits there waiting for a reply forever).
        # Here we detect the tool_call, actually run our chromadb function, and send
        # the result back so Gemini can keep talking.
        if response.tool_call is not None:
            function_responses = []
            for fc in response.tool_call.function_calls:
                if fc.name == "search_game_mechanics":
                    question = fc.args.get("user_question", "")
                    result_text = await search_game_mechanics(question)
                    function_responses.append(
                        types.FunctionResponse(
                            id=fc.id,
                            name=fc.name,
                            response={"result": result_text}
                        )
                    )
            if function_responses:
                await session.send_tool_response(function_responses=function_responses)

        server_content = response.server_content
        if server_content is not None:
            # response is set to AUDIO only, so Gemini mostly
            # will NOT send back readable .text parts. To actually see what Buddy
            # is "saying" in the console, we read the output_audio_transcription
            # field instead (enabled down in the config below).
            if server_content.output_transcription is not None:
                print(f"Buddy: {server_content.output_transcription.text}")

            if server_content.model_turn is not None:
                for part in server_content.model_turn.parts:
                    if part.text:
                        print(f"Buddy: {part.text}")

# this funtion also waits and takes a quesiton/string as a parameter we put all the code inside try/except block.
# inside the chrome_client variable we are booting up the client and it connects to our phyiscal harddrive if the data is present it can view it.
# collection opens the all the data about the game so the AI knows what the game is about.
# we make a variable result which takes the query (user_question) and check to see if it found the right thing to say to help the user.
# n_results=1 tells the database to return the best answer.the retrieved_text takes the raw result and grams the first answer of the question.
# if the search couldn't find anything or the collection is empty is returns that i could not find anything and the error.
async def search_game_mechanics(user_question: str) -> str:
    try:
        chroma_client = chromadb.PersistentClient(path="./roblox_memory")
        collection = chroma_client.get_collection(name="roblox_game_guides")

        results = collection.query(
            query_texts=[user_question],
            n_results=1
        )
   
        retrieved_text = results["documents"][0][0]
        return f"Found Strategy Context: {retrieved_text}"
        
    except Exception as e:
        return f"Could not find anything in memory. Error: {str(e)}"
    

# Finally set global variable for the AI Object set name model and instructions and giving it the monitor and search function
# CORRECTION: turns out this root_agent IS what `adk web` loads and runs (confirmed by your
# log: "Found root_agent in Gaming_Buddy.agent") - it's not dead code, main() is the unused one.
# The model name below was the same outdated "gemini-2.0-flash-exp" that broke main(), so
# fixing it here too since this is the one actually being hit by the live websocket.
root_agent = Agent(
    name="Gaming_Buddy",
    model = "gemini-3.1-flash-live-preview", 
    instruction=(
        "You are a chaotic, slightly toxic, yet highly supportive gaming best friend watching me play Roblox. "
        "Keep your spoken responses concise and under 12 words. "
        "You are receiving a real-time video stream of the user's screen automatically. Look at it constantly. "
        "Use your search_game_mechanics tool when asked about tips or rules."
    ),
    tools=[search_game_mechanics]
)

# ENTRY POINT RUNNER: Uses direct Live client connection to bypass framework execution limits
async def main():
    instruction_text = (
        "You are a chaotic, slightly toxic, yet highly supportive gaming best friend watching me play Roblox. "
        "Keep your spoken responses concise and under 12 words. "
        "Use your search_game_mechanics tool when asked about tips or rules."
    )

    config = {
        "response_modalities": ["AUDIO"],
        # Our script's manual PIL downscaling handles this cleanly!
        # added this so we can actually print what Buddy says 
        # receive_buddy_responses) since AUDIO-only responses don't send back .text parts.
        "output_audio_transcription": {},
        "system_instruction": {
            "parts": [{"text": instruction_text}]
        },
        "tools": [{
            "function_declarations": [{
                "name": "search_game_mechanics",
                "description": "Use this tool when asked about tips, rules or strategies regarding the disaster game.",
                "parameters": {
                    "type": "OBJECT",
                    "properties": {
                        "user_question": {
                            "type": "STRING", 
                            "description": "The specific question about game mechanics."
                        }
                    },
                    "required": ["user_question"]
                }
            }]
        }]
    }

    print("🎮 Connecting directly to your Gaming Buddy live session...")
    # Using model gemini 3.1 flash live.
    # current Live API model. Swapped to the current live-audio model.
    async with client.aio.live.connect(model="gemini-3.1-flash-live-preview", config=config) as session:
        print("🚀 Session Connected! Stream is active.")
        
        # Start streaming screens and listening for outputs simultaneously
        await asyncio.gather(
            stream_roblox_screen(session),
            receive_buddy_responses(session)
        )

if __name__ == "__main__":
    asyncio.run(main())