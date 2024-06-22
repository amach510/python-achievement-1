import pickle

# Define function for take recipes
def take_recipe():
    name = input("Enter name of the recipe: ")
    cooking_time = int(input("Enter the cooking time of the recipe in minutes: "))
    ingredients = input("Enter the ingredients needed (separated by commas): ").split(', ')
    difficulty = calc_difficulty(cooking_time, ingredients)
    return {
        "name": name,
        "cooking_time": cooking_time,
        "ingredients": ingredients,
        "difficulty": difficulty
    }

# Define function for calculating recipe difficulty
def calc_difficulty(cooking_time, ingredients):
    ingredients_len = len(ingredients)

    if cooking_time < 10 and ingredients_len < 4:
        difficulty = "Easy"
    elif cooking_time < 10 and ingredients_len >= 4:
        difficulty = "Medium"
    elif cooking_time >= 10 and ingredients_len < 4:
        difficulty = "Intermediate"
    elif cooking_time >= 10 and ingredients_len > 4:
        difficulty = "Hard"
    
    return difficulty

# [Main code] User enter filename to attempt opening a binary file (read mode)
filename = input("Enter the filename of your recipe (without extension): ")
filename = filename + '.bin'
try:
    file = open(filename, "rb")
    data = pickle.load(file)
except FileNotFoundError:
    print("File doesn't exist.")
    data = {
        "recipes_list": [],
        "all_ingredients": []
    }
except:
    print("An unexpected error occurred.")
    data = {
        "recipes_list": [],
        "all_ingredients": []
    }
else:
    file.close()
finally:
    recipes_list = data["recipes_list"]
    all_ingredients = data["all_ingredients"]

# Ask user how many recipes they would like to enter
n = int(input("Enter how many recipes you would like to enter: "))

#For-loop calling take_recipe() function
for i in range(n):
    recipe = take_recipe()
    recipes_list.append(recipe)
    for ingredient in recipe['ingredients']:
        if ingredient not in all_ingredients:
            all_ingredients.append(ingredient)

# Gather the updated recipes_list and all_ingredients
data = {
    "recipes_list": recipes_list,
    "all_ingredients": all_ingredients
}

# Open binary file
with open(filename, "wb") as file:
    pickle.dump(data,file)