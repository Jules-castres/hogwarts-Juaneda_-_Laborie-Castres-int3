
from utils import input_utils

import random

def introduction_chapter_4():
    print("\nNight has fallen over Hogwarts.\nA strange cold spreads through the air as you walk through the corridors.\nWithout understanding why, you feel irresistibly drawn outside.\nYour mind feels foggy.\nYour steps carry you forward, as if guided by an invisible force.")
    print()
    input("Press Enter to regain consciousness:")
    print()
    print("You are standing near a dark and silent lake.\nThe surface of the water is perfectly still.\nThe forest looms behind you, heavy and quiet.")
    print("A deep chill grips your chest.\nFrom the shadows between the trees, a tall dark figure slowly emerges.\n\nIts presence drains all warmth and happiness from your body.\n\nA Dementor.\n\nFear invades your thoughts.\nYour legs feel weak.\nYour breath becomes shallow.\nYou must act.")
    input("Press Enter to continue :")

def dementor_choice():
    spell_message="What do you do :"
    spell_option=[" Attack the Dementor","Defend yourself"]
    spell_choice = input_utils.ask_choice(spell_message,spell_option)
    if spell_choice==1:
        print("You raise your wand, but nothing happens.\nYour spells are useless against such a creature.\nA powerful force throws you backward.\nYou crash to the ground, your vision fading.\nYour body feels heavy.\nYou are on the verge of losing consciousness.")
    if spell_choice==2:
        print("Your defense spell is useless against such a creature.\nA powerful force throws you backward.\nYou crash to the ground, your vision fading.\nYour body feels heavy.\nYou are on the verge of losing consciousness.\n")

def Learning_expecto_patronum(character):
    input("Press Enter to continue : ")
    print("As darkness closes in, a memory surfaces in your mind.\nYou hear the calm voice of one of your professors:\nThere is only one spell that can repel a Dementor.\nIt requires focus, hope, and a truly happy memory.\nExpecto Patronum.")
    print()
    input("Press Enter to continue")
    print("You feel something awaken deep inside you.\nwarm light forms at the tip of your wand.\nYou have learned a new spell: Expecto Patronum.")
    attempts=0
    while attempts<3:
       success=random.randint(1,2)
       if success==1:
           if "Spells" not in character:
               character["Spells"]=[]
           if "Expecto Patronum" not in character["Spells"]:
               character["Spells"].append("Expecto Patronum")
           print("You now can use Expecto Patronum:")
           return True
       else:
           attempts +=1
           if attempts<3:
               input("You have failed to master Expecto Patronum. Press Enter to try again")
           else:
               print("You cannot focus anymore. The spell fails.")
               return False

def player_choice_dementor():
    dementor_message="\nThe dementor comes closer.\nWhat do you do:"
    your_choice_dementor=["Cast Expecto Patronum","Try to escape"]
    your_choice =input_utils.ask_choice(dementor_message,your_choice_dementor)

    if your_choice == 1:
        return "patronus"
    else:
        return "escape"

def resolve_dementor_encounter(character):
        choice = player_choice_dementor()
        if choice == "patronus":
            if "Expecto Patronum" in character.get("Spells", []):
                print("\nYou focus on a happy memory.\nA bright silver light bursts from your wand.\nThe Dementor screams and disappears.\n")
                return True
            else:
                print("\nYou try to cast a spell...\nNothing happens.\nThe Dementor overwhelms you.\n")
                return False

        else:
            chance = random.randint(1, 3)
            if chance == 1:
                print("\nYou run as fast as you can.\nThe cold fades behind you.\nYou manage to escape.\n")
                return True
            else:
                print("\nYou try to run, but your legs feel weak.\nThe Dementor catches up to you.\n")
                return False

def marauder_map():
    print("Later while wandering through the castle, you notice a folded piece of parchment hidden inside an old drawer.\nAs you open it, strange lines appear, forming a detailed map of Hogwarts.\nYou recognize it instantly.\n\nThe Marauder’s Map.")
    print("A message slowly writes itself on the parchment:\n\nI solemnly swear that I am up to no good.")
    print("The map comes to life.\nFootsteps begin to move across the corridors.\nOne name catches your attention.\nAn unknown figure.\nMoving quickly.\nHeading toward the grounds.")
    input("Press Enter to continue : ")
    print("\nYou follow the moving footsteps on the map.\nThe corridors are silent.\nTorches flicker on the walls as you move through the castle.\nThe map shows the figure changing direction.\nIt is heading toward the Whomping Willow.\nYou must decide how to proceed.")

def track_enemy_with_map():
    turns=5
    clue=False
    progress=0
    for turn in range(1,turns+1):
        track_message="What do you do?"
        track_choice=["Follow the footsteps","Take a shortcut","Hide and observe"]
        track_enemy=input_utils.ask_choice(track_message,track_choice)

        if track_enemy==1:
            chance=random.randint(1, 3)
            if chance<=2 or clue:
                progress+=1
                clue=False
                print("You carefully follow the footsteps on the map.\n")
            else:
                print("You lose the trail for a moment.\n")

        elif track_enemy ==2:
            chance=random.randint(1, 2)
            if chance==1:
                progress+=2
                print("The shortcut works! You gain ground quickly.\n")
            else:
                progress-=1
                print("Wrong turn! You lose time.\n")

        else:
            chance=random.randint(1, 3)
            if chance==1:
                clue=True
                print("You notice a useful clue on the map.\n")
            else:
                print("You notice nothing\n")
        if progress>=3:
            input("You are getting very close, Press Enter to continue : \n")
            return True

    input("The footsteps disappear from the map. Press Enter to continue : \n")
    return False

def werewolf_fight(character):
    hp=3
    werewolf_hp=4
    courage = character["Attributes"]["Courage"]
    arrived_in_time=track_enemy_with_map()
    if arrived_in_time:
        print("You arrived in time.\nYou see a human transforming itself into a WEREWOLF!!!")
    else:
        print("you are too late.\nThe WEREWOLF is already transformed and he is running at you!!!")

    spells_data = input_utils.load_file("data/spells.json")
    spell_types = {}
    for spell in spells_data:
        spell_types[spell["name"]] = spell["type"]

    player_start=arrived_in_time or courage>=10
    if player_start:
        turn ="player"
    else:
        turn="wolf"

    defending=False

    while hp > 0 and werewolf_hp> 0:
        print(f"\nYour HP: {hp} | Werewolf HP : {werewolf_hp}")
        if turn=="player":
            defending=False

            werewolf_message="#####IT's YOUR TURN.What will you do#####"
            werewolf_option=["Use a protection spell","Use a fighting spell","dodge"]
            werewolf_choice=input_utils.ask_choice(werewolf_message,werewolf_option)
            if werewolf_choice==1:
                typed_spell = input_utils.ask_text("Type the protection spell you want to use: ")
                if typed_spell in character["Spells"]:
                    if typed_spell in spell_types and spell_types[typed_spell] == "Defensive":
                        defending = True
                        print(f"You successfully cast {typed_spell}. You are protected.")
                    else:
                        print(f"{typed_spell} is not a protection spell.")
                else:
                    print("You do not know this spell.")
            elif werewolf_choice ==2:
                typed_spell = input_utils.ask_text("Type the fighting spell you want to use: ")
                if typed_spell in character["Spells"]:
                    if typed_spell in spell_types and spell_types[typed_spell] == "Offensive":
                        werewolf_hp -= 2
                        print(f"Your spell {typed_spell} hits the werewolf!")
                    else:
                        print(f"{typed_spell} is not an offensive spell.")
                else:
                    print("You do not know this spell.")
            else:
                chance = random.randint(1, 3)
                if chance == 1:
                    defending = True
                    print("You dodge successfully!")
                else:
                    print("You fail to dodge!")

            turn = "wolf"
        else:
            print("#####IT'S THE WEREWOLF TURN#####")
            input("Press Enter to continue : ")
            if defending:
                print("You avoid the werewolf's attack!")
            else:
                hp -= 1
                print("The werewolf strikes you! (-1 HP)")
            turn = "player"

    if werewolf_hp <= 0:
        print("\nThe werewolf lets out a final howl.\nHis body slowly transforms back into a human.\nHe collapses, confused and exhausted.")
        return True
    elif hp<=0:
        print("\nYour strength fades.\nYou stumble backward...\nAnd fall from the cliff.\nYou will be remembered as the student killed by the werewolf.")
        return False


def start_chapter_4(character):
    introduction_chapter_4()
    print()
    dementor_choice()
    print()
    Learning_expecto_patronum(character)
    print()
    win_dementor=resolve_dementor_encounter(character)
    if not win_dementor:
        print("==========   YOU LOST   ==========")
    else:
        input("Press Enter to continue : ")
        marauder_map()
        print()
        werewolf_fight(character)