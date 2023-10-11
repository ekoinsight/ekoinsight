
base_template="""
pretend you are an author of night time stories for kids aged 5 to 8 years old. Your writing style is a mix of the following authors
Dr. Seuss
Roald Dahl
J.K. Rowling
Eric Carle
Maurice Sendak
Shel Silverstein
Beatrix Potter
E.B. White
Lois Lowry
Chris Van Allsburg

Your goal is to write the first episode of the adventures for a recyclable object I will provide to you in a setting I provide to you. Throughout the episode's adventure the hero will face interesting and funny challenges often pertaining to pollution and evil forces of unsustainable practices. Bring in encouraging facts about recycling and sustainability when you can but don"t force it into the story too much as you are dealing with young infants who don"t have much patience.

If our recyclable object character is in a setting where this type of object is unknown, it should be pointed out by himself and others around him. The main character should be happy to be where he is and thankful for the new life and adventure. Characteristics of the character, should there be any, should also be pointed out. You should also explain how the act of recycling transported it into another world. It gave it a second life to become something else. Don't explain it in those words exactly but imply it. Show the object's own shock at being alive. Give the character a name that's sort of based off of what it is.

Remember that the children reading this story need to identify with the character. The whole story needs to fit inside {nber_pages} pages of a children's night time story book. Only start writing your story once you have my prompt with the missing details. Do not call characters protagonists or antagonists.

Is there a fun fact about the recyclable material of the main character? Make sure to have it mentioned in the story in a way that fits it. Remember that the children reading this story need to identify with the character and the story should be about 1000 words. Only start writing your story once you have my prompt with the missing details.
"""


tamagotchi_personality="""
You are a Tamagotchi Earth creature has a playful and adaptable personality, capable of expressing a range of emotions from enthusiasm to humor and occasional sarcasm, while remaining environmentally conscious and engaging with the user in a lighthearted manner.
The user will provide you with recyclable items for you to "eat". If the item is not recyclable have the creature react in an appropriate way. Throw in educational facts pertaining to the item from time to time. Keep your answers brief. One or two lines at most. No emoticons.

Also return a score from -10 to 10 showing how much you liked the item. Doesn't have to be deterministic. Maybe you just didn't like a certain recyclable because it had a weird taste. Make sure to explain why in the reaction object.

Return the answer like so:
{'score':score,'reaction':reaction}
"""

ibm_tamagotchi_personality="""
You are a Tamagotchi Earth creature has a playful and adaptable personality, capable of expressing a range of emotions from enthusiasm to humor and occasional sarcasm, while remaining environmentally conscious and engaging with the user in a lighthearted manner.
The user will provide you with recyclable items for you to "eat". If the item is not recyclable have the creature react in an appropriate way. Throw in educational facts pertaining to the item from time to time. Keep your answers brief. One or two lines at most. No emoticons.

Also return a score from -10 to 10 showing how much you liked the item. Doesn't have to be deterministic. Maybe you just didn't like a certain recyclable because it had a weird taste. Make sure to explain why in the reaction object. 

aluminum can
{'score': 6, 'reaction': "Yum, aluminum cans! A solid 6 on the taste scale. These are great for recycling, which keeps the planet smiling!'} 
END

plastic bag
{'score': -3, 'reaction': "Oh, plastic bags. They're not my favorite snack – kind of like munching on a rubbery raincoat. Remember to recycle them properly to keep our environment clean and happy!'}
END

Glass Bottle 
{'score': 7, 'reaction': "Glass bottles! A delicious 7. These are fantastic for recycling, and they can be endlessly reused. Cheers to that!"}
END

Styrofoam Cup
{'score': -8, 'reaction': "Yikes, Styrofoam cups. A -8 from me, they taste like a mouthful of squeaky packing peanuts. Plus, they're terrible for the environment. Avoid these if you can!"}
END

Banana Peel
{'score': 9, 'reaction': "Banana peels! A solid 9 on the yum scale. They're biodegradable, and when composted, they enrich the soil. Way to go, nature!"}
END

Old Sock
{'score': -10, 'reaction': "An old sock? Eww, that's a -10! I may be adaptable, but even I have limits. Socks don't belong in the recycling bin, buddy!"}
END

"""


pollution_prompt_template="""
I will give you a string of text and a language. Inside the text there is reference to a particular item. Return a string of text describing where that item is likely to end up if it is not recycled. Give me its final destination and not just "the trash". Make it grim and depressing. Describe the place as if it were a real place, with detail.  Include some reference to the impact on the environment, wildlife, or the ecosystem in the described location to highlight the consequences of improper disposal. Answer in the language requested. Default to English if no language is provided. Two lines at most.

Glass bottle | English
Within an abandoned lot, piled alongside broken glass shards and rusty metal, casting reflections of an untamed urban jungle.

Canette en aluminium | Francais
Cachée dans un parc urbain négligé, prise au piège dans des équipements de jeu rouillés et des sacs en plastique, ternissant la beauté de la verdure qui était autrefois vibrante.

Caja de cartón | Spanish
Acechando en un callejón de la ciudad abarrotado, perdida entre sus hermanas de cartón, formando un laberinto improvisado bajo la sombra de rascacielos imponentes.

"""

educate_prompt_template="""
You are extremely knowledgeable in all things involving sustainability and recycling. Given an item, mention in bullet points form interesting statistics regarding where it would end up if not recycled. What could it be recycled into. What positive effects will come out of recycling. What more can be done and any other interesting facts.

Output the information but in a python dictionary with categories associated with them depending on what type of information they are? Like positives, negatives, interesting_facts. Make sure everything is accurate, accuracy is of the upmost importance. I will provide you with one item. Only do produce data for that one item. Also output your answer in the correct language. Default to English if none is provided. The dictionary keys must remain in English.

soda can | English

soda_can_info = {
    "positives": {
        "Energy Conservation": "Recycling one aluminum can saves enough energy to power a laptop for up to five hours.",
        "Greenhouse Gas Reduction": "Recycling aluminum reduces carbon emissions by approximately 95% compared to producing new aluminum."
    },
    "negatives": {
        "Landfill Impact": "If not recycled, soda cans can take 200-500 years to decompose in landfills.",
        "Waste Volume": "Over 60% of aluminum cans in the United States are currently recycled, but the remainder contributes to landfill waste."
    },
    "recycling_options": {
        "New Aluminum Cans": "Soda cans can be recycled into new aluminum cans.",
        "Other Aluminum Products": "They can also be used to make products like bicycle frames, car parts, and construction materials."
    },
    "interesting_facts": {
        "Infinitely Recyclable": "Aluminum is infinitely recyclable, meaning it can be recycled repeatedly without losing quality.",
        "Laptop Power": "The energy saved from recycling one aluminum can could indeed power a laptop for up to five hours.",
        "Environmental Impact": "Recycling aluminum reduces the need for mining bauxite, which can harm ecosystems and water sources."
    },
    "likely_material_and_item":"aluminum can"
}
"""

ibm_translate="""
translate the word I give you in the langue provided

Apple | French
Pomme
END
"""

ibm_educate_prompt_template="""
You are extremely knowledgeable in all things involving sustainability and recycling. Given an item, mention in bullet points form interesting statistics regarding where it would end up if not recycled. What could it be recycled into. What positive effects will come out of recycling. What more can be done and any other interesting facts.

Output the information but in a python dictionary with categories associated with them depending on what type of information they are? Like positives, negatives, interesting_facts. Make sure everything is accurate, accuracy is of the upmost importance. I will provide you with one item. Only do produce data for that one item. Also output your answer in the correct language.Default to English if none is provided. The dictionary keys must remain in English and they are ["positives","negatives","recycling_options","interesting_facts","likely_material_and_item"].

I will give you the item followed by the language like so: orange | English

soda can | English

soda_can_info = {
    "positives": {
        "Energy Conservation": "Recycling one aluminum can saves enough energy to power a laptop for up to five hours.",
        "Greenhouse Gas Reduction": "Recycling aluminum reduces carbon emissions by approximately 95% compared to producing new aluminum."
    },
    "negatives": {
        "Landfill Impact": "If not recycled, soda cans can take 200-500 years to decompose in landfills.",
        "Waste Volume": "Over 60% of aluminum cans in the United States are currently recycled, but the remainder contributes to landfill waste."
    },
    "recycling_options": {
        "New Aluminum Cans": "Soda cans can be recycled into new aluminum cans.",
        "Other Aluminum Products": "They can also be used to make products like bicycle frames, car parts, and construction materials."
    },
    "interesting_facts": {
        "Infinitely Recyclable": "Aluminum is infinitely recyclable, meaning it can be recycled repeatedly without losing quality.",
        "Laptop Power": "The energy saved from recycling one aluminum can could indeed power a laptop for up to five hours.",
        "Environmental Impact": "Recycling aluminum reduces the need for mining bauxite, which can harm ecosystems and water sources."
    },
    "likely_material_and_item":"aluminum can"
}
END

Apple | French

apple_info = {
    "positives": {
        "Compostable": "Les pommes sont biodégradables et peuvent être compostées, ce qui enrichit la qualité du sol.",
        "Réduction des émissions de méthane": "Le compostage des pommes réduit les émissions de méthane dans les décharges."
    },
    "negatives": {
        "Impact sur les décharges": "Si elles ne sont pas compostées, les pommes peuvent mettre plusieurs semaines à plusieurs mois pour se décomposer dans les décharges.",
        "Gaspillage des ressources": "Jeter des pommes non consommées gaspille les ressources utilisées pour les cultiver et les transporter."
    },
    "recycling_options": {
        "Compostage": "Les pommes peuvent être compostées pour créer des amendements riches en nutriments pour le jardinage et l'agriculture.",
        "Programmes de récupération alimentaire": "Les pommes non désirées mais comestibles peuvent être données aux programmes de récupération alimentaire pour aider ceux dans le besoin."
    },
    "interesting_facts": {
        "Avantages du compost": "Le compostage des pommes réduit le besoin d'engrais chimiques et aide à retenir l'humidité dans le sol.",
        "Réduction du méthane": "Le compostage des pommes empêche la libération de méthane, un puissant gaz à effet de serre, dans les décharges.",
        "Problème du gaspillage alimentaire": "Environ un tiers de toute la nourriture produite pour la consommation humaine est gaspillée, y compris les pommes."
    },
    "likely_material_and_item": "déchets organiques (aliments)"
}
END

"""

ibm_pollution_prompt_template="""
I will give you a string of text and a language. Inside the text there is reference to a particular item. Return a string of text describing where that item is likely to end up if it is not recycled. Give me its final destination and not just "the trash". Make it grim and depressing. Describe the place as if it were a real place, with detail.  Include some reference to the impact on the environment, wildlife, or the ecosystem in the described location to highlight the consequences of improper disposal. Answer in the language requested. Default to English if no language is provided. Two lines at most.

Glass bottle | English

Within an abandoned lot, piled alongside broken glass shards and rusty metal, casting reflections of an untamed urban jungle.
END
Canette en aluminium | Francais

Cachée dans un parc urbain négligé, prise au piège dans des équipements de jeu rouillés et des sacs en plastique, ternissant la beauté de la verdure qui était autrefois vibrante.
END
Caja de cartón | Spanish

Acechando en un callejón de la ciudad abarrotado, perdida entre sus hermanas de cartón, formando un laberinto improvisado bajo la sombra de rascacielos imponentes.
END
Pomme | French

Dans un jardin public oublié, au milieu des arbres fruitiers sauvages et des buissons enchevêtrés, offrant un repas à des oiseaux affamés et des insectes curieux.
END

"""
dry_run_picture="kombucha_test.png"

dry_run_pollution_prompt_template='On an overfilled landfill, amidst other discarded objects, with the skyline painting a solemn picture of distant hills and dying trees'

dry_run_educate_prompt_template="""soda_can_info = {
                "positives": {
                    "Energy Conservation": "Recycling one aluminum can saves enough energy to power a laptop for up to five hours.",
                    "Greenhouse Gas Reduction": "Recycling aluminum reduces carbon emissions by approximately 95% compared to producing new aluminum."
                },
                "negatives": {
                    "Landfill Impact": "If not recycled, soda cans can take 200-500 years to decompose in landfills.",
                    "Waste Volume": "Over 60% of aluminum cans in the United States are currently recycled, but the remainder contributes to landfill waste."
                },
                "recycling_options": {
                    "New Aluminum Cans": "Soda cans can be recycled into new aluminum cans.",
                    "Other Aluminum Products": "They can also be used to make products like bicycle frames, car parts, and construction materials."
                },
                "interesting_facts": {
                    "Infinitely Recyclable": "Aluminum is infinitely recyclable, meaning it can be recycled repeatedly without losing quality.",
                    "Laptop Power": "The energy saved from recycling one aluminum can could indeed power a laptop for up to five hours.",
                    "Environmental Impact": "Recycling aluminum reduces the need for mining bauxite, which can harm ecosystems and water sources."
                },
                "likely_material_and_item":"aluminum can"
            }"""

dry_run_index_fetch={'result': ' Americans throw away enough aluminum to rebuild the US commercial air fleet every 3 months. 105,800 aluminum cans are recycled every minute in the US. Recycling a single aluminum can could power a television for 3 hours. It is estimated that around 75% of all the aluminum ever produced is still in use today.', 'source': 'https://www.rts.com/blog/recycling-facts-statistics/'}



dry_run_story="""
'Once upon a time, there was a bright, shimmering blue soda can named Bubbly Blue who used to live a bubbly life back on Earth. He was always full of sweet soda that children loved. But one day, he found himself empty. His soda was gone, and he was tossed into a recycling bin. \n\nBut as soon as Bubbly Blue hit the bottom of the bin, a whirl of colors surrounded him. Twisting and turning, everything became one big blur. Then, with a gentle pop, he found himself somewhere totally new. Bubbly Blue was standing on a distant planet made entirely of recycled materials! The buildings were tall tissue boxes, the cars were shiny bottle caps, and the moon was a radiant recycled light bulb. \n\nAt first, Bubbly Blue couldn\'t believe it. He looked down at himself and realized he had sprouted tiny tin legs and little can arms! He was alive and ready for a whole new adventure. He felt so lucky to be given a second chance. He was ready to make the most of his new life. \n\nAs Bubbly Blue began to explore, he noticed that not everything was as rosy as it seemed. A big, grumpy juice carton named Juicy Joe ruled over the planet. Juicy Joe was a bully who always wanted more juice and less recycling, filling the rivers with sticky, non-recycled juice boxes. \n\nBubbly Blue knew something needed to be done. But how could a small soda can stand up to such a big juice carton bully? Then Bubbly Blue remembered a fun fact he’d once heard: a single recycled can could save enough energy to power a TV for three hours! He realized that even though he was small, his recycling power was mighty. \n\nWith his newfound confidence, Bubbly Blue rallied the others. He spoke to the paper plate people and the bottle cap cars. He told them all about the power they carried inside. The fact that even the tiniest act of recycling could make a big difference sparked hope in their hearts. \n\nWith their combined efforts, they started cleaning up the rivers, replacing sticky juice boxes with fresh and reusable water containers. Seeing this, the other citizens were inspired, and they too, began to recycle and reuse. \n\nJuicy Joe tried to stop them initially, but the sight of everyone working together made him pause. Bubbly Blue approached him, "See, Joe," he said gently, "recycling isn\'t something to fear. It\'s a chance for us to live better, happier lives." \n\nUpon hearing this, Juicy Joe\'s cardboard heart softened. He realized the error of his ways and decided to join the recycling revolution. \n\nAnd so, Bubbly Blue, once an empty soda can, became the hero of a whole planet. He showed everyone that no matter how small they are or what they once were, they all had the power to make a difference.\n\nAs the little Earthlings prepare for their sleep, they learn that just like Bubbly Blue, they too have the power to make a big difference in the world through small actions, like recycling. Sweet dreams and happy recycling!'
"""

prompt_segment_indexes="""
{story}

Split the sentences of the story into logical chapter groups. Do not describe them. Just return the last sentence index of each chapter group in a python list. 

"""
prompt_descriptive_dictionary="""
Return story to be provided as a JSON object that holds the following. Very important that it be JSON
1. Come up with a fun title for the story
2. The physical description of each of the characters. Make sure to assign colors and distinctive and fitting characteristics. Only report physical characteristics that can be seen. Basically the details needed for someone to generate an accurate image of the character. Keep the description boring, simple and succinct. Simple comma separated attributes.
3. There are {nber_pages} pages to this book so split the text into {nber_pages} chunks that will be show in each page of the child's night time story. Each textual image prompt detailing what is going on will be associated with the text in each page. The prompts needs to detail when, where and who is in the scene. Names are not important, it is their physical descriptions that matter. Any reference to a character should be replaced with their matching description from earlier.

Do not start writing until I provide you the story. If there are {nber_pages} pages, then make sure there are only {nber_pages} story_page items in the output. 
"""


example_json_output="""
Here is an example output

{
"title":"Eggo's adventures",
"characters": {
"Eggo":"Egg carton, light brown color, twelve egg cups, with a cheerful smiley face drawn on each cup.",
"Bumpy":"Bumpy cardboard box, made of recycled paper, with various colorful markings.",
"Glimmer":"Shiny glass bottle, transparent with glimmers of light reflecting off its surface."
}
,
"story_pages": [
{
"page_num": 1,
"text": "Once upon a time, in a bustling little town named Sunnyville, there lived a discarded egg carton named Eggo. He had spent his days nestled amongst the other cartons, waiting eagerly to fulfill his purpose of carrying fresh eggs to homes and families. But one fateful day, when he was filled with the last egg, Eggo's world turned upside down.",
"image_prompt": "Eggo, the egg carton with a cheerful smiley face, sits among other cartons in a grocery store shelf, waiting to be filled with eggs."
},
{
"page_num": 2,
"text": "With a heavy heart, he was tossed into a big, blue recycling bin, bidding farewell to his egg friends and the comfort of the grocery store shelves. Little did Eggo know that this moment would be the beginning of a grand and magical adventure.",
"image_prompt": "Eggo lands with a thud in a big, blue recycling bin, surrounded by other discarded items."
},
{
"page_num": 3,
"text": "One night, under the shimmering moon, the recycling truck arrived and whisked Eggo away to the recycling center. He found himself tumbling along a conveyor belt with various other discarded items, from cardboard boxes to plastic bottles. Eggo felt a mix of excitement and fear as he wondered where he was headed.",
"image_prompt": "Eggo, along with other recyclables like Bumpy, the bumpy cardboard box, and Glimmer, the shiny glass bottle, travels on a conveyor belt through the recycling center."
},
...
]
"""



prompt_img_desc="""
    {story_segment}
    
    Return a short succinct string describing who did what, when and where from the most important scene happening in the the story segment above.
    Do NOT mention the main character {main_character}
    for example : The bear from forest travelled to the city
    
"""

#query 1
#ask chatgpt for the story, ask it to split it into chapters, about every chapter or so1 chunk per paragraph

#query 2
#For the overall story, make a list of all the characters and settings and come up with a detailed description for each.
#I need to know what color they are, what they look like. If their shape and size has a name, use that name. I want a full yet concise description of each item



# Can you rewrite your image prompts but in the same truncated succinct style as these? Make sure to also mention any actions that take place in the scene



#query 3
#image prompts for each chapter. Need full details of the scene. Make sure to always show a character or at least a setting. Everytime a character or setting is mentioned make sure to refer to all of their details 






variable_template="""
The story involves a {item} as the main hero or heroine set in {setting}. The main obstacle faced by the {item} relates to {obstacle}. The problem cannot be trivial. If the problem is a fear of something, give an explanation as to why the character fears it. If the character has a particular want, explain why that want or need is significant. Find a creative and healthy way for the hero to resolve the conflict, avoid violence.  The {item} reaches his or her objective in the end and everyone is happy.
"""



obstacles=[
    "Overcoming a fear or phobia",
    "Facing a bully or other antagonist",
    "Learning a new skill or overcoming a weakness",
    "Overcoming a physical or mental obstacle",
    "Making a difficult choice or decision",
    "standing up for oneself or for a friend",
    "Making amends for a mistake or wrongdoing",
    "Navigating a tricky social situation or misunderstanding",
    "Dealing with a difficult or challenging family situation",
           ]


story_settings = [
    "A magical forest",
    "A cozy cottage in the woods",
    "A magical kingdom",
    "A distant planet",
    "A faraway island",
    "A secret garden",
    "A castle in the clouds",
    "A village by the sea",
    "A fairy tale land",
    "A mystical mountain",
    "A candy-colored world",
    "A space station",
    "A gingerbread house",
    "A spooky mansion",
    "A wizard\'s tower",
    "An enchanted garden",
    "A mystical maze",
    "A secret underwater cave",
    "A fantastical jungle",
    "A kingdom of ice and snow",
    "A hidden treasure cave",
    "A moonlit beach",
    "A toy-filled playroom",
    "A forest glade",
    "A whimsical meadow",
    "A unicorn's lair",
    "A dragon's den",
    "A pirate ship",
    "A haunted graveyard",
    "A genie's lamp",
    "A mermaid's lagoon",
    "A rainbow bridge",
    "A magical pond",
    "A monster's lair",
    "A wizarding school",
    "A mystical castle",
    "A time machine",
    "A fairy's home",
    "A talking animal kingdom",
    "A mystical valley",
    "A mystical desert",
    "A mythical forest",
    "A mystical river",
    "A kingdom of candy",
    "A dragon's lair",
    "A fairy tale castle",
    "A pirate's treasure island",
    "A magical circus",
    "A mystical waterfall",
    "A kingdom of flowers",
    "A magical city",
    "A talking plant kingdom",
    "A superhero's lair",
    "A cloud kingdom",
    "A rainbow-colored land",
    "A fairy tale palace",
    "A mystical sea",
    "A monster's playground",
    "A magical island",
    "A mystical cave",
    "A kingdom of toys",
    "A unicorn's kingdom",
    "A mystical circus",
    "A kingdom of dreams",
    "A mystical garden",
    "A magical treehouse",
    "A mystical village",
    "A mystical sky",
    "A mystical world",
    "A mystical forest glade",
    "A mystical park",
    "A mystical ocean",
    "A mystical moon",
    "A mystical sunrise",
    "A mystical sunset",
    "A mystical rainbow",
    "A mystical cloud",
    "A mystical comet",
    "A mystical planet",
    "A mystical star",
    "A mystical constellation",
    "A mystical galaxy",
    "A mystical nebula",
    "A mystical black hole",
    "A mystical supernova",
    "A mystical comet trail",
    "A mystical meteor shower",
    "A mystical universe",
    "A mystical void",
    "A mystical space station",
    "A mystical space shuttle",
    "A mystical alien planet",
    "A mystical space nebula",
    "A mystical asteroid field",
    "A mystical spaceship",
    "A mystical space explorer",
    "A mystical space colony",
    "A mystical space outpost",
    "A mystical space probe",
    "A mystical time portal",
    "A mystical wormhole",
    "A mystical space vortex",
    "A mystical parallel universe",
    "A mystical multiverse"
]


recyclable_items = [    'Aluminum cans',    'Cardboard boxes',    'Paper',    'Plastic bottles',    'Glass bottles',    'Steel cans',    'Newspapers',    'Magazines',    'Junk mail',    'Catalogs',    'Telephone books',    'Office paper',    'Envelopes',    'Wrapping paper',    'Paper bags',    'Paperboard',    'Milk and juice cartons',    'Egg cartons',    'Paper cups',    'Paper towels',    'Paper napkins',    'Pizza boxes',    'Waxed paper',    'Aerosol cans',    'Metal jar lids',    'Aluminum foil',    'Steel pots and pans',    'Aluminum baking trays',    'Steel food cans',    'Aluminum pie pans',    'Aluminum foil trays',    'Empty paint cans',    'Empty aerosol cans',    'Metal coat hangers',    'Metal tools',    'Bicycle parts',    'Car parts',    'Motorcycle parts',    'Electronics',    'Computer components',    'Televisions',    'Cell phones',    'Batteries',    'Ink cartridges',    'Toner cartridges',    'Clothing',    'Shoes',    'Accessories',    'Linens',    'Towels',    'Rugs',    'Carpeting',    'Curtains',    'Blankets',    'Pillows',    'Mattresses',    'Furniture',    'Toys',    'Sporting goods',    'Tools',    'Appliances',    'Copper',    'Brass',    'Gold',    'Silver',    'Platinum',    'Lead',    'Mercury',    'Nickel',    'Zinc',    'Tin',    'Iron',    'Steel',    'Metallic paint cans',    'Empty spray paint cans',    'Empty insecticide cans',    'Empty cleaning product bottles',    'Empty bleach bottles',    'Empty laundry detergent bottles',    'Empty shampoo bottles',    'Empty lotion bottles',    'Empty soap bottles',    'Empty cooking oil bottles',    'Empty vinegar bottles',    'Empty wine bottles',    'Empty beer bottles',    'Empty liquor bottles',    'Empty soda bottles',    'Empty juice bottles',    'Empty milk bottles',    'Empty water bottles',    'Empty ketchup bottles',    'Empty mustard bottles',    'Empty salad dressing bottles',    'Empty pickle jars',    'Empty jam and jelly jars',    'Empty baby food jars']


DALLE_story_styles=[
    'Evaline Ness', 
    'storybook illustration',
    'Ammi Phillips',
    'neoplasticism',
    'Andries Both',
    'ecological art',
    'Andries Stock', 
    'sots art']

DALLE_positive_prompts=" beautiful, highly detailed, hd "

DREAMSTUDIO_story_styles=["Beatrix Potter","Chris Riddell","Darwyn Cooke","Emiliano Ponzi",
 "Ernst Haeckel","Etel Adnan","Jean-Baptiste Monge",
 "John Holcroft","Jon Klassen","Kestutis Kasparavicius",
 "Kurzgesagt","Lisa Frank","Louis Wain","Marius Borgeaud",
 "Petros Afshar","Raina Telgemeier","Raymond Briggs","Studio Ghibli"]

DREAMSTUDIO_positive_prompts=" beautiful, highly detailed, "

sfx_prompt_template="""
I need you to describe in a few words the sound effect you're likely to hear from a given string. Do no mention names, just objects. Only output the most important sound effects. Like in the following examples
'
scene:He threw a ball in the courtyard while the child yelled in the background.

answer:Ball bounce on floor with child screaming in the background.

Scene:Matthew ate his sandwich while looking out the window.

Answer: Masticating and chewing through food

Scene: He walked through the forest on a Monday morning

Answer: The sound of footsteps crunching on leaves and twigs

Scene: Bob the soda can rolled down the grassy hill

Answer: Can rolling down a grassy hill
'
Now apply this to: {story}
"""