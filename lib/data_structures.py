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
    for spicy_food in spicy_foods:
        print(spicy_food["name"])

print(get_names(spicy_foods))        

def get_spiciest_foods(spicy_foods):
    spiciest_foods = []
    for food in spicy_foods:
        if food.get('heat_level', 0) > 5:
            spiciest_foods.append(food)
    return spiciest_foods
print(get_spiciest_foods(spicy_foods)) 
    

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food.get('name', 'Unknown')
        cuisine = food.get('cuisine', 'Unknown')
        heat_level = food.get('heat_level', 0)
        heat_emojis = '🌶' * heat_level
        print(f"{name} ({cuisine}) | Heat Level: {heat_emojis}")

print_spicy_foods(spicy_foods)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
     for food in spicy_foods:
        if food.get('cuisine', '').lower() == cuisine.lower():
            return food

print(get_spicy_food_by_cuisine(spicy_foods, 'Thai'))
print(get_spicy_food_by_cuisine(spicy_foods, 'American'))

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        return[food for food in spicy_foods if food.get('heat_level', 0) > 5]
    
print(print_spiciest_foods(spicy_foods))        

def get_average_heat_level(spicy_foods):
    if not spicy_foods:
        return 0 
    
    total_heat = sum(food.get('heat_level', 0) for food in spicy_foods)
    number_of_foods = len(spicy_foods)
    average_heat = total_heat / number_of_foods
    return average_heat

print(get_average_heat_level(spicy_foods))

def create_spicy_food(spicy_food):
    spicy_food = {
    'name': 'Griot',
    'cuisine': 'Haitian',
    'heat_level': 10,
    }
    spicy_foods.append(spicy_food)
    return spicy_foods

print(create_spicy_food(spicy_foods))

