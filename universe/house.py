from utils import input_utils
def update_house_point(houses,house_name,points):

    for name in houses.keys():
        if name == house_name:
            houses[name] += points

def display_winning_house(houses):

    house = []
    point = 0
    for name in houses.keys():
        if houses[name] > point:
            point = houses[name]
    for h in houses.keys():
        if houses[h] == point:
            house.append(h)
    if len(house) > 1:
        print(f'The {", ".join(house)} houses are the winners with {point} points !')
    elif len(house) == 1:
        print(f'The house {", ".join(house)} is the winner with {point} points !')

def assign_house(character, questions):

    houses = {"Gryffindor": 0,
            "Slytherin": 0,
            "Hufflepuff": 0,
            "Ravenclaw": 0,
            }

    for i in character["Attributes"].keys():
        if i == "Courage":
            update_house_point(houses, "Gryffindor", 2*character["Attributes"][i])
        elif i == "Ambition":
            update_house_point(houses, "Slytherin", 2*character["Attributes"][i])
        elif i == "Loyalty":
            update_house_point(houses, "Hufflepuff", 2*character["Attributes"][i])
        elif i == "Intelligence":
            update_house_point(houses, "Ravenclaw", 2*character["Attributes"][i])

    for question in questions:
        a = input_utils.ask_choice(question[0],question[1])
        update_house_point(houses, question[2][a-1], 3)

    print("\nSummary of scores:")
    max_point = 0
    name_house = ""
    for name in houses.keys():
        print(f'{name}: {houses[name]} points')
        if houses[name] > max_point:
            name_house = name
            max_point = houses[name]
    return name_house
