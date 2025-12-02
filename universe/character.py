def init_character(last_name,first_name,attributes):
    """
    The def will return your character information
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

def modify_money(characters,amount):
    characters["money"]+=amount
    return characters["money"]

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
