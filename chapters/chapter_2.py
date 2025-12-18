from utils import input_utils
from universe import character as module_char

def meets_friends(character):
    print("You board the Hogwarts Express. The train slowly departs northward... \nA red-haired boy enters your compartment, looking friendly. ")
    print("Hi! I'm Ron Weasley. Mind if I sit with you? ")
    ron_message="How do you respond? "
    ron_choice_1=["Sure, have a seat!"," Sorry, I prefer to travel alone."]
    ron_choice=input_utils.ask_choice(ron_message,ron_choice_1)
    if ron_choice==1:
        for i in character['Attributes'].keys():
            if i=='Loyalty':
                character['Attributes'][i]+=1
        print("Ron smiles: — Awesome! You'll see, Hogwarts is amazing! \n")
    elif ron_choice==2:
        for j in character['Attributes'].keys():
            if j=='Ambition':
                character['Attributes'][j]+=1
        print("Ron is crying away from you: -I want my Mommy OUINOUIN BOUHOUHOU \n")
    print("A girl enters next, already carrying a stack of books. ")
    print("Hello, I'm Hermione Granger. Have you ever read 'A History of Magic'?")
    Hermione_message="How do you respond?"
    hermione_choice_1=["Yes, I love learning new things!","Uh… no, I prefer adventures over books."]
    hermione_choice=input_utils.ask_choice(Hermione_message,hermione_choice_1)
    if hermione_choice==1:
        for k in character['Attributes'].keys():
            if k=='Intelligence':
                character['Attributes'][k]+=1
        print("Hermione smiles, impressed: — Oh, that's rare! You must be very clever! \n")
    elif hermione_choice==2:
        for h in character['Attributes'].keys():
            if h=='Courage':
                character['Attributes'][h]+=1
        print("Hermione is disappointed: -I wasn't expecting anything from you and i'm still disappointed. \n")

    print("Then a blonde boy enters, looking arrogant. ")
    print("I'm Draco Malfoy. It's best to choose your friends carefully from the start, don't you think? ")
    DracoMalfoy_message="How do you respond?"
    DracoMalfoy_choice_1=["Shake his hand politely.","Ignore him completely.","Respond with arrogance."]
    DracoMalfoy_choice=input_utils.ask_choice(DracoMalfoy_message,DracoMalfoy_choice_1)
    if DracoMalfoy_choice==1:
        for Draco_1 in character['Attributes'].keys():
            if Draco_1=='Ambition':
                character['Attributes'][Draco_1]+=1
        print("Draco with a haughty smile: - Good choice.You must Know my father. \n")
    elif DracoMalfoy_choice==2:
        for Draco_2 in character['Attributes'].keys():
            if Draco_2=='Loyalty':
                character['Attributes'][Draco_2]+=1
        print("Draco frowns, annoyed. — You'll regret that! \n")
    elif DracoMalfoy_choice==3:
        for Draco_3 in character['Attributes'].keys():
            if Draco_3=='Courage':
                character['Attributes'][Draco_3]+=1
        print("Draco frowned: - You mustn't know who my father is.I'll make you regret it.\n")
    print("The train continues its journey. Hogwarts Castle appears on the horizon... \n\nYour choices already say a lot about your personality!")
    print(f"Your updated attributes: {character["Attributes"]}")

def enter_common_room(character):
    houses = input_utils.load_file("../data/houses.json")
    character_house = houses[character["House"]]
    print("\nYou follow the prefects through the castle corridors...")
    print(character_house['emoji'], character_house['description'])
    print(character_house['installation_message'])
    colors = ", ".join(character_house['colors'])
    print("\nYour house colors:", colors)
