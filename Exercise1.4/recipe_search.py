import pickle

# Define a function to display a recipe
def display_recipe(recipe):
    print("Recipe:", recipe["name"])
    print("Cooking Time (minutes):", str(recipe["cooking_time"]))
    print("Ingredients:")
    for ingredient in recipe["ingredients"]:
        print(ingredient)
    print("Difficulty level:", recipe["difficulty"])
    print("")

# Define a function to search for an ingredient
def search_ingredient(data):
    all_ingredients = data["all_ingredients"]
    recipes_list = data["recipes_list"]
    for position, ingredient in enumerate(all_ingredients):
        print("Ingredient " + str(position) + ": " + ingredient)
    try:
        ingredient_index = int(input("Enter the number of the ingredient you would like to search for: "))
        ingredient_searched = all_ingredients[ingredient_index]
    except ValueError:
        print("One or more of your inputs aren't numbers.")
    except IndexError:
        print("The number you chose is not in the list.")
    except:
        print("An unexpected error occurred.")
    else:
        for recipe in recipes_list:
            if ingredient_searched in recipe["ingredients"]:
                display_recipe(recipe)

# Main Code
filename = input("Enter the filename where you've stored your recipe (without extension): ")
filename = filename + '.bin'
try:
    file = open(filename, "rb")
    data = pickle.load(file)
except FileNotFoundError:
    print("File doesn't exist.")
except:
    print("An unexpected error occurred.")
else:
    search_ingredient(data)
    file.close()