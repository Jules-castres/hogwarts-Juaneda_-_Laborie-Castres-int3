from universe import character as char_module
from utils import input_utils


def introduction():

    print("=" * 60)
    print("     WELCOME TO THE WIZARDING WORLD")
    print("=" * 60)
    print()

    print("You live an ordinary life with your aunt and uncle,")
    print("in the cupboard under the stairs at 4 Privet Drive.")
    input("Press Enter to continue...")
    print()

    print("But everything is about to change...")
    print()
    print("Strange events are happening around you.")
    print("Mysterious letters arrive by the hundreds.")
    input("Press Enter to continue...")
    print()

    print("And tonight, at precisely midnight, someone knocks at the door.")
    print()
    print("Your destiny as a wizard awaits you at Hogwarts!")
    print()
    print("=" * 60)
    input("Press Enter to begin your adventure...")
    print()

def create_character():
    """
    The function create a character
    from the information given by the user.
    :return: display_character
    """
    attribute = {"Courage":0,"Intelligence":0, "Loyalty":0, "Ambition":0}
    name = input_utils.ask_text("Enter your character's last name: ")
    first_name = input_utils.ask_text("Enter your character's first name: ")
    print("Choose your attributes:")
    for i in attribute.keys():
        number = input_utils.ask_number(f'{i} level (1-10) : ', 1,10)
        attribute[i] = number

    character = char_module.init_character(str(name), str(first_name), attribute)
    char_module.display_character(character)
    return character


def receive_letter():

    print("An owl flies through the window, delivering a letter")
    print("sealed with the Hogwarts crest...")
    input("Press Enter to open the letter...")
    print()

    print("=" * 60)
    print("                    HOGWARTS SCHOOL")
    print("              of WITCHCRAFT and WIZARDRY")
    print("=" * 60)
    print()
    print("Dear Student,")
    print()
    print("We are pleased to inform you that you have been accepted")
    print("to Hogwarts School of Witchcraft and Wizardry!")
    print()
    print("Term begins on September 1st.")
    print()
    print("Please find enclosed a list of all necessary books")
    print("and equipment.")
    print()
    print("Yours sincerely,")
    print()
    print("Minerva McGonagall")
    print("Deputy Headmistress")
    print("=" * 60)
    input("Press Enter to continue...")
    print()

    choice = input_utils.ask_choice("Do you accept this invitation and go to Hogwarts?",
                        ["Yes, of course!", "No, I'd rather stay with Uncle Vernon..."])

    if choice == "No, I'd rather stay with Uncle Vernon...":
        print()
        print("You tear up the letter, and Uncle Vernon cheers:")
        print()
        print('"EXCELLENT! Finally, someone NORMAL in this house!"')
        print()
        print("The magical world will never know you existed...")
        print("Game over.")
        print()
        exit(0)
    else:
        print()
        print("You accept the invitation with excitement!")
        print("Your magical adventure is about to begin...")
        input("Press Enter to continue...")
        print()


def meet_hagrid(character):

    print("\n A giant man appears at the door, covered in snow.\n")

    print('Hagrid: "Hello ' + character["First Name"] + '! I\'m Rubeus Hagrid.')
    print('        I\'m here to help you with your shopping on Diagon Alley."')
    input("Press Enter to continue...")
    print()

    choice = input_utils.ask_choice("Do you want to follow Hagrid?", ["Yes", "No"])
    print()

    if choice == "No":
        print('Hagrid chuckles: "Come on now! You need your school supplies!"')
        input("Press Enter to continue...")
        print("\nHagrid gently insists and takes you along anyway!\n")
    else:
        print('Hagrid smiles: "Excellent! Let\'s get going then!"\n')

    input("Press Enter to continue...")
    print("Hagrid leads you towards Diagon Alley...\n")

def buy_supplies(character):

    print("Welcome to Diagon Alley!")
    print()
    print("There the catalog of available items:")

    inventory =  input_utils.load_file("data/inventory.json")
    required = ["Magic Wand","Wizard Robe","Potions Book"]

    for i in inventory.keys():
        if inventory[i][0] in required:
            print(f'{i}: {inventory[i][0]} - {inventory[i][1]} Galleons (required)')
        else:
            print(f'{i}: {inventory[i][0]} - {inventory[i][1]} Galleons')

    while required != []:
        print(f"\nYou have {character["Money"]} Galleons.")
        print("Remaining required items:", end=" ")
        for j in required:
            if j != required[-1]:
                print(j, end=", ")
            else:
                print(j)
        item_number = input_utils.ask_number("Enter the number of the item to buy: ", 1, len(inventory))

        item_key = str(item_number)
        selected_name = inventory[item_key][0]
        selected_price = inventory[item_key][1]

        if character['Money'] < selected_price:
            print("Not enough money! Game over.")
            exit(0)

        print(f"You bought: {selected_name} (-{selected_price} Galleons).")
        char_module.modify_money(character, -selected_price)
        char_module.add_item(character, "Inventory", selected_name)

        if selected_name in required:
            required.remove(selected_name)

    print("\nAll required items have been purchased!")
    print("\nIt's time to choose your Hogwarts pet!")

    print(f"\nYou have {character["Money"]} Galleons.")
    print("Available pets: ")

    pets = {
    "1": ["Owl", 20],
    "2": ["Cat", 15],
    "3": ["Rat", 10],
    "4": ["Toad", 5]
    }
    animal = []
    for pet in pets.keys():
        print(f'{pet}: {pets[pet][0]} - {pets[pet][1]} Galleons')
        animal.append(pets[pet][0])
    a = input_utils.ask_choice("Which pet do you want ?", animal)
    print(f"You chose: {pets[str(a)][0]} (-{pets[str(a)][1]} Galleons).")
    char_module.add_item(character, "Inventory", pets[str(a)][0])
    print("\nAll required items have been successfully purchased! Here is your final inventory: ")
    return char_module.display_character(character)

def start_chapter_1():
    introduction()
    char = create_character()
    receive_letter()
    meet_hagrid(char)
    buy_supplies(char)
    print("End of the Chapter 1 ! The magic awakens as your adventure starts at Hogwarts... ")
    return char
