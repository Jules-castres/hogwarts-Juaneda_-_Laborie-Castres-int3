#Classes and Discovering Hogwarts
from universe import character as char_module
from utils import input_utils
from universe import house
import random

def learn_spells(character, file_path="data/spells.json"):

    all_spells = input_utils.load_file(file_path)
    print("You begin your magic lessons at Hogwarts...")

    offensive_spells = []
    defensive_spells = []
    utility_spells = []

    for spell in all_spells:
        if spell["type"] == "Offensive":
            offensive_spells.append(spell)
        elif spell["type"] == "Defensive":
            defensive_spells.append(spell)
        elif spell["type"] == "Utility":
            utility_spells.append(spell)

    learned_spells = []

    if offensive_spells:
        chosen = random.choice(offensive_spells)
        learned_spells.append(chosen)
        print(f"\nYou have just learned the spell: {chosen['name']} ({chosen['type']})")
        input("Press Enter to continue...")

    if defensive_spells:
        chosen = random.choice(defensive_spells)
        learned_spells.append(chosen)
        print(f"\nYou have just learned the spell: {chosen['name']} ({chosen['type']})")
        input("Press Enter to continue...")

    count = 0
    while count < 3 and utility_spells:
        chosen = random.choice(utility_spells)
        if chosen not in learned_spells:
            learned_spells.append(chosen)
            print(f"\nYou have just learned the spell: {chosen['name']} ({chosen['type']})")
            input("Press Enter to continue...")
            count += 1

    for spell in learned_spells:
        char_module.add_item(character, "Spells", spell["name"])

    print("\n" + "=" * 60)
    print("You have completed your basic spell training at Hogwarts!")
    print("Here are the spells you now master:")
    print("=" * 60)

    for spell in learned_spells:
        print(f"- {spell['name']} ({spell['type']}): {spell['description']}")

    print("=" * 60)

def magic_quiz(character,  file_path="data/magic_quiz.json"):

    magic_quiz = input_utils.load_file(file_path)
    questions = []
    points = 0
    print('\nWelcome to the Hogwarts magic quiz ! ')
    print('Answer the 4 questions correctly to earn points for your house.')

    for i in range(1,5):
        chosen = random.choice(magic_quiz)
        while chosen in questions:
            chosen = random.choice(magic_quiz)
        #print(chosen['answer'])
        questions.append(chosen)
        print(f'{i}. {chosen["question"]}')
        answer = input("> ")
        if answer == chosen["answer"]:
            points += 25
            print('Correct answer! +25 points for your house.')
        else :
            print(f'Wrong answer. The correct answer was: {chosen["answer"]}')
    print(f'Score obtained: {points} points')
    character['Points'] = points
    return character

def start_chapter_3(character, houses):
    learn_spells(character)
    magic_quiz(character)
    house.update_house_point(houses, character['House'], character['Points'])
    house.display_winning_house(houses)
    char_module.display_character(character)
    print("\nEnd chapter 3, well done !! You are now a certified wizard...")

