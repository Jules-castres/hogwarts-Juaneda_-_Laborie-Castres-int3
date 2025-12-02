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
