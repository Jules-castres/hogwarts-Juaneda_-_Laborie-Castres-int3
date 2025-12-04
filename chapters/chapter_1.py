from universe import character
from utils import input_utils
def introduction():
    """
    the function displays a text of introduction for the chapter 1
    :return: None
    """
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
    first_name = input_utils.ask_text("Enter your character's last name: ")
    print("Choose your attributes:")
    for i in attribute.keys():
        number = input_utils.ask_number(f'{i} level (1-10 : ', 1,10)
        attribute[i] = number
    character.display_character(character.init_character(name, first_name, attribute))