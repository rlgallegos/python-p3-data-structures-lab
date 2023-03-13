spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    new_list = [each["name"] for each in spicy_foods]
    return new_list

def get_spiciest_foods(spicy_foods):
    new_list = [each for each in spicy_foods if each["heat_level"] > 5]
    return new_list

def print_spicy_foods(spicy_foods):
    for each in spicy_foods:
        print(f'{each["name"]} ({each["cuisine"]}) | Heat Level: ' + "🌶" * each["heat_level"])

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for each in spicy_foods:
        if each["cuisine"] == cuisine:
            return each

def print_spiciest_foods(spicy_foods):
    new_list = [each for each in spicy_foods if each["heat_level"] > 5]
    for each in new_list:
        print(f'{each["name"]} ({each["cuisine"]}) | Heat Level: ' + "🌶" * each["heat_level"])


def get_average_heat_level(spicy_foods):
    sum_of_heat = sum([each["heat_level"] for each in spicy_foods])
    return sum_of_heat / len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

