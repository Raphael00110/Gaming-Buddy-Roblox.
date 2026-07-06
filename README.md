# 🎮 Gaming Buddy: Real-Time AI Roblox Assistant
An advanced, low-latency AI gaming companion that "watches" your live Roblox gameplay and acts as a chaotic, highly supportive best friend. Powered by the Google GenAI Live API and vector search capabilities.

---

## 🚀 Key Architectural Features
Unlike basic AI wrappers that sequentially make slow HTTP requests or read/write frames to disk, this agent uses a customized async pipeline designed for high-performance deployment:

* **Direct RAM-to-WebSocket Streaming:** Captures desktop screenshots and streams them entirely in volatile memory (`io.BytesIO`) straight up a persistent WebSocket connection. This completely eliminates slow physical disk I/O operations (`current_frame.jpg` bottlenecks) and keeps game loop performance impact minimal.
* **Low-Latency Live Handshake:** Configured to interface directly with low-latency multimodal endpoints, maintaining steady frame delivery and audio processing asynchronously via `asyncio.gather`.
* **RAG-Powered Game Mechanics Sync:** Integrates a local **ChromaDB** vector database instance. When asked specialized strategy questions, the agent queries semantic embeddings stored locally to fetch precise game tactics in real-time.
* **Bypassed Execution Layer Wrapper:** Bypasses rigid CLI runtime restrictions by injecting custom orchestration loops, allowing it to act as both an independent service and a standard modular application package.

---

## 🛠️ Project Structure
```text
Gaming_Buddy/
├── agent.py              # Main execution entry-point & WebSocket orchestration loop
├── VisionAnalysis.py     # Local vision processing extensions
├── teach.py              # Script for populating the knowledge base vector embeddings
├── roblox_memory/        # ChromaDB persistent storage folder (ignored by Git)
├── .env                  # Private API Key repository variables (ignored by Git)
└── __init__.py           # Explicit package layout registration for the Google ADK

## 💻 Language and Tools
- Python
- ChromeDB
- asyncio
- Google lib
- PIL
- json and env



---(Installation)---

~Install the necessary system dependencies using pip:

-pip install google-genai chromadb pillow python-dotenv

~ Environment Configuration

- Create a .env file in the root directory to store your API credentials securely:
    Code snippet
    GEMINI_API_KEY=your_actual_google_api_key_here

~Execution

Launch the live companion session directly via your standard Command Prompt or Terminal:
fist by going to the project folder and running the command : python -m google.adk.cli web .
after that go to http://localhost:8000/ or the IP provided

Note: This project still needs improvements.