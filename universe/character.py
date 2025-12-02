def display_character(character):
    """
    The function displays all information of character depending on their type.
    :param character: dict
    :return: None
    """
    print("Character profile:")
    for i in character.keys():
        if type(character[i]) == dict:
            print(i, ":")
            for j in character[i].keys():
                print(f"-{j}: {character[i][j]}")
        elif type(character[i]) == list:
            print(f'{i}: {", ".join(character[i])}')
        else:
            print(f'{i}: {character[i]}')