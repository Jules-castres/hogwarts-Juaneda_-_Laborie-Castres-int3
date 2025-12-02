def update_house_point(houses,house_name,points):
    """
    The function add or subtract "points" from "house_name" in houses.
    :param houses: dict
    :param house_name: string
    :param points: int
    :return: None
    """
    for name in houses.keys():
        if name == house_name:
            houses[name] += points