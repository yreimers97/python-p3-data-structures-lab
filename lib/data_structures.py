import ipdb

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

spicy_food = [
    {
        "name": 'Griot', 
        "cuisine": 'Haitian', 
        "heat_level": 10,
    },
]

def get_names(spicy_foods):
    food_names = [names['name'] for names in spicy_foods]
    return food_names

def get_spiciest_foods(spicy_foods):
    spiciest = [spicy for spicy in spicy_foods if spicy['heat_level'] > 5]
    return spiciest
  

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {"🌶" * food["heat_level"]}')

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food_type in spicy_foods:
        if food_type["cuisine"] == cuisine:
            return food_type

def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)


def get_average_heat_level(spicy_foods):
    average = sum(food['heat_level'] for food in spicy_foods) / len(spicy_foods)
    return  average

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods