from pydantic import BaseModel, Field 

# BaseModel forces the AI to reply ONLY in this exact format.
# Field acts as the guard, ensuring the data fits your strict rules.
class VisionAnalysis(BaseModel):
    
    # Rule: Must be True or False. 
    # The description acts as prompt instructions telling the AI WHEN to pick True or False.
    significant_change_detected: bool = Field(
        description="True if something major happened (death, win, boss spawn, low health), False if it is normal gameplay."
    )
    
    # Rule: Must be text (a string). 
    # The description tells the AI exactly WHAT kind of joke to write in this text box.
    funny_reaction_text: str = Field(
        description="A hilarious, quick commentary about what is happening on screen in the game."
    )
