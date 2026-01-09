def init_character(last_name,first_name,attributes):

    character={"Last Name":last_name,
    "First Name": first_name,
    "Money":100,
    "Inventory": [],
    "Spells": [],
    "Attributes": attributes }
    return character


def modify_money(characters, amount):

    characters["Money"] += amount

def add_item(character, key, item):

    character[key].append(item)
    return character

def display_character(character):

    print("\nCharacter profile :")
    print()
    for i in character.keys():
        if type(character[i]) == dict:
            print(i,":")
            for j in character[i].keys():
                print(f"-{j}: {character[i][j]}")
        elif type(character[i]) == list:
            print(f'{i}: {", ".join(character[i])}')
        else:
            print(f'{i}: {character[i]}')
