import chromadb #import the chromedb library used for Vector database.

disaster_guides = [
    {
        "id": "NDS_FLASH_FLOOD",
        "game": "Natural Disaster Survival",
        "category": "Disaster",
        "text": "Flash Flood: The sea level rises rapidly and destroys lower parts of structures. Anyone touching the water loses health. Strategy: Seek higher ground immediately. Avoid unstable tall structures like the yellow brick tower because they will fall over. Stand on structurally stable mid-to-high points."
    },
    {
        "id": "NDS_METEOR_SHOWER",
        "game": "Natural Disaster Survival",
        "category": "Disaster",
        "text": "Meteor Shower: Large flaming meteors crash down from the sky, destroying buildings and killing players on impact. Strategy: Stay in wide-open outdoor spaces so you can look up, see the meteors falling, and dodge the impact zones. Do not hide inside buildings, as collapsing bricks will crush you."
    },
    {
        "id": "NDS_EARTHQUAKE",
        "game": "Natural Disaster Survival",
        "category": "Disaster",
        "text": "Earthquake: The ground shakes violently, causing tall buildings to sway, break apart, and collapse. Strategy: Run away from all buildings immediately and head to flat, open grassland. Stay away from any debris or falling parts."
    },
    {
        "id": "NDS_FIRE",
        "game": "Natural Disaster Survival",
        "category": "Disaster",
        "text": "Fire: Fires start randomly and spread rapidly across objects and structures. Touching flaming blocks drains health. Strategy: Stay on the basic green grass, as grass does not catch fire. Do not climb high up into buildings because you will get trapped when the lower floors burn down."
    },
    {
        "id": "NDS_TORNADO",
        "game": "Natural Disaster Survival",
        "category": "Disaster",
        "text": "Tornado: A massive spinning funnel moves across the map, sucking up blocks and players, flinging them into the map boundaries. Strategy: Stay on ground level and actively run in the opposite direction of the tornado. Do not stand inside buildings, as they will get torn apart with you inside."
    },
    {
        "id": "NDS_THUNDERSTORM",
        "game": "Natural Disaster Survival",
        "category": "Disaster",
        "text": "Thunderstorm: Lightning strikes the map every two seconds, targeting the highest physical points on the island. Strategy: Avoid high, open, and metallic places. Stay on the ground level or hide inside the lower floor of a sturdy building to block the lightning strikes."
    },
    {
        "id": "NDS_TSUNAMI",
        "game": "Natural Disaster Survival",
        "category": "Disaster",
        "text": "Tsunami: A massive wall of water sweeps across the entire island from one side, wiping out anything in its path. Strategy: Look at the ocean to spot which direction the wave is coming from. Quickly climb to the back side of a tall, sturdy building so the building absorbs the impact of the wave for you."
    },
    {
        "id": "NDS_BLIZZARD",
        "game": "Natural Disaster Survival",
        "category": "Disaster",
        "text": "Blizzard: Extreme cold and freezing winds damage players who are exposed to the open air, causing hypothermia. Strategy: Get inside a building immediately and stay away from open windows or doors. If you stay outside, your health will rapidly tick down to zero."
    },
    {
        "id": "NDS_ACID_RAIN",
        "game": "Natural Disaster Survival",
        "category": "Disaster",
        "text": "Acid Rain: Corrosive rain falls from toxic green clouds, slowly melting buildings and destroying player health on contact. Strategy: Get under a solid roof immediately. Keep an eye on the roof above you; if the acid melts through it completely, you must quickly move under a new, undamaged ceiling."
    },
    {
        "id": "NDS_VOLCANO",
        "game": "Natural Disaster Survival",
        "category": "Disaster",
        "text": "Volcanic Eruption: A massive volcano spawns in the center of the map, spewing explosive lava bricks into the air. Strategy: Run to the absolute furthest edges of the map away from the volcano. Stay in an open space so you can watch the sky and step aside to dodge rolling lava rocks."
    },
    {
        "id": "NDS_SANDSTORM",
        "game": "Natural Disaster Survival",
        "category": "Disaster",
        "text": "Sandstorm: A heavy yellow dust storm blindingly limits your vision while high winds throw loose bricks and debris around. Strategy: Sit down or stay low to the ground near a solid, low wall. Watch out for flying loose objects, as they will inflict heavy damage if they hit you."
    },
    {
        "id": "NDS_DEADLY_VIRUS",
        "game": "Natural Disaster Survival",
        "category": "Disaster",
        "text": "Deadly Virus: A random player becomes infected and starts coughing. Anyone who stands close to an infected player will catch the virus and lose health. Strategy: Stay completely away from other players. Run to an isolated corner of the map. If someone runs toward you, run away immediately."
    },
    {
        "id": "NDS_DUAL_FLOOD_METEOR",
        "game": "Natural Disaster Survival",
        "category": "Dual Disaster",
        "text": "Dual Disaster (Flash Flood + Meteor Shower): This is a deadly contradiction. Floods force you high, but meteors destroy high buildings. Strategy: Find a wide, flat, medium-height structure or rock. Stay exposed to the sky so you can actively dodge meteors while staying just high enough to avoid touching the rising flood water."
    },
    {
        "id": "NDS_DUAL_TSUNAMI_BLIZZARD",
        "game": "Natural Disaster Survival",
        "category": "Dual Disaster",
        "text": "Dual Disaster (Tsunami + Blizzard): Tsunami forces you to stand outside behind buildings, but Blizzard freezes you if you stay outside. Strategy: Stay inside a sturdy building until the absolute last second before the Tsunami wave hits, then step behind the outer wall to block the wave. As soon as the wave passes, run right back inside to stop freezing."
    },
    {
        "id": "NDS_DUAL_FIRE_EARTHQUAKE",
        "game": "Natural Disaster Survival",
        "category": "Dual Disaster",
        "text": "Dual Disaster (Fire + Earthquake): Buildings collapse from the shaking while structures simultaneously burn down. Strategy: Run to the flat green grass plains immediately. Do not step on loose bricks because they might be on fire or fall on top of you."
    },
    {
        "id": "NDS_ITEM_BALLOON",
        "game": "Natural Disaster Survival",
        "category": "Item",
        "text": "Green Balloon Gamepass: An equippable tool that reduces your gravity when held. Strategy: Use it to jump higher and slowly float downwards. This is highly effective for completely negating fall damage when jumping off collapsing towers or escaping floods."
    },
    {
        "id": "NDS_ITEM_APPLE",
        "game": "Natural Disaster Survival",
        "category": "Item",
        "text": "Red Apple Gamepass: An item that heals your Roblox character when consumed. Strategy: Because passive health regeneration does not exist in this game, the Red Apple is the only way to restore your health bar after taking damage from a disaster."
    },
    {
        "id": "NDS_FALL_DAMAGE",
        "game": "Natural Disaster Survival",
        "category": "Mechanic",
        "text": "Fall Damage and Resetting: The game features steep fall damage penalties. Because your health does not automatically regenerate, if you survive a disaster but have very low health, it is best to manually reset your character or jump off the lobby tower before the next round starts to refresh your health bar."
        },
    
  {
        "id": "NDS_MAPS_LIST",
        "game": "Natural Disaster Survival",
        "category": "Maps",
        "text": "Official Maps List: The game features maps like Glass Office, Surf Central, Launch Land, Happy Home, Sunshine Airport, Raving Raceway, Coastal Quickstop, and Fort Indestructible. Strategy: Each map has unique structures. Glass melts in acid rain, while bricks collapse easily during earthquakes."
    },
    {
        "id": "NDS_ROCKET_LAUNCH",
        "game": "Natural Disaster Survival",
        "category": "Secret Mechanic",
        "text": "Launch Land Rocket: On the Launch Land map, there is a giant rocket. If players board it before it launches, they fly into space. However, if a disaster hits the rocket during launch, it will explode, killing everyone inside."
    },
    {
        "id": "NDS_LOBBY_METEOR",
        "game": "Natural Disaster Survival",
        "category": "Easter Egg",
        "text": "Lobby Disasters: When you are dead or waiting in the main glass lobby tower, disasters cannot hurt you. However, a giant meteor occasionally strikes the lobby directly between rounds, smashing the glass and flinging players around."
    },
    {
        "id": "NDS_COMPASS_ITEM",
        "game": "Natural Disaster Survival",
        "category": "Item",
        "text": "Disaster Compass Gamepass: A map tool item that displays the exact name of the incoming disaster a few seconds before it officially starts. Strategy: Use it to get a head start on finding the perfect hiding spot before other players realize what the disaster is."
    }

    
]


# creates or opens database folder on computer storage.
chroma_client = chromadb.PersistentClient(path ="./roblox_memory")
# creates a space collection for a specific topic like a guide to a game in roblox.
collection = chroma_client.get_or_create_collection(name="roblox_game_guides")


collection.add(
    documents=[item["text"] for item in disaster_guides],
    metadatas=[{"game": item["game"], "category": item["category"]} for item in disaster_guides],
    ids=[item["id"] for item in disaster_guides]
)
print(f"Successfully saved all {len(disaster_guides)} data packs to your Vector Database!")

# set the variable result in which your asking the collection a question and it gives the first result it finds
results = collection.query(
    query_texts=["What do I do in a flood?"],
    n_results=1
)

# Print out the document text it found
print("\n--- Test Query Result ---")
print(results["documents"][0][0])
