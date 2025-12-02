def init_character(last_name,first_name,attributes):
    """
    The function will return your character information
    :param last_name: string
    :param first_name: string
    :param attributes: dictionary
    :return: dictionary
    """
    character={"Last Name":last_name,
    "First Name": first_name,
    "Money":100,
    "Inventory": [],
    "Spells": [],
    "Attributes": attributes }
    return character


def modify_money(characters, amount):
    """
    function will return the modification of the money
    :param characters: dictionary
    :param amount: integer
    :return: none
    """
    characters["money"] += amount

def add_item(character, key, item):
    """
    Adds an item (string) to one of the character's list fields.
    :param character: dictionary
    :param key: string
    :param item: string
    :return:dictionary
    """
    character[key].append(item)
    return character

def display_character(character):
    """
    The function displays profile information by taking types into account.
    :param character: dict
    :return: None
    """
    print("Character profile :")
    for i in character.keys():
        if type(character[i]) == dict:
            print(i,":")
            for j in character[i].keys():
                print(f"-{j}: {character[i][j]}")
        elif type(character[i]) == list:
            print(f'{i}: {", ".join(character[i])}')
        else:
            print(f'{i}: {character[i]}')
