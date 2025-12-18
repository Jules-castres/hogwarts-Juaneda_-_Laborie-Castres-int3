from utils import input_utils
from chapters import chapter_1, chapter_2, chapter_3
def display_main_menu():
    return input_utils.ask_choice("Welcome back !",["1. Start Chapter 1 - Arrival in the magical world.","2. Exit the game."])

def launch_menu_choice():
    """
    The function display the choices to begin the game
    :return: none
    """
    houses = {
        "Gryffindor": 0,
        "Slytherin": 0,
        "Hufflepuff": 0,
        "Ravenclaw": 0
    }
    choice = display_main_menu()
    if choice == 2:
        print("Well I think it is a goodbye ! See you soon !")
        exit(0)
    elif choice == 1:
        character = chapter_1.start_chapter_1()
        chapter_2.start_chapter_2(character)
        chapter_3.start_chapter_3(character, houses)