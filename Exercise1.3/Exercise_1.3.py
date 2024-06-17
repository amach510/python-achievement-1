# Initailize two empty lists.
recipes_list=[]
ingredients_list=[]

# Define function take_recipe.
def take_recipe():
    name = input("Enter the name of the recipe: ")
    cooking_time = int(input("Enter the cooking time of the recipe in minutes: "))
    ingredients = input("Enter ingredients (separated by commas): ").split(',')
    recipe = {
        "name": name,
        "cooking_time": cooking_time,
        "ingredients": ingredients
    }
    return recipe

# User inputs how many recipes they would like to enter
n = int(input("Enter how many recipes you would like to enter: "))

# First for-loop
for i in range(n):
    recipe = take_recipe()
    
    # Loop through each ingredient in the current recipe
    for ingredient in recipe['ingredients']:
        if ingredient not in ingredients_list:
            ingredients_list.append(ingredient)
    recipes_list.append(recipe)

# Second for-loop
for recipe in recipes_list:
    cooking_time = recipe["cooking_time"]
    ingredients_len = len(recipe["ingredients"])
    difficulty = ""

    if cooking_time < 10 and ingredients_len < 4:
        recipe["difficulty"] = "Easy"
    elif cooking_time < 10 and ingredients_len >= 4:
        recipe ["difficulty"] = "Medium"
    elif cooking_time >= 10 and ingredients_len < 4:
        recipe ["difficulty"] = "Intermediate"
    elif cooking_time >= 10 and ingredients_len > 4:
        recipe ["difficulty"] = "Hard"

    print ("Recipe:", recipe["name"])
    print ("Cooking Time (minutes):", str(recipe["cooking_time"]))
    print ("Ingredients:")
    for ingredient in recipe["ingredients"]:
        print(ingredient.strip())
    print ("Difficulty level:", recipe ["difficulty"])
    print("")

# Print all ingredients of all recipes
print ("Ingredients Available Across All Recipes")
print("")
for ingredient in sorted(ingredients_list):
    print(ingredient.strip())