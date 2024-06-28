class Recipe:
    def __init__(self, name):
        self.name = name
        self.ingredients = []
        self.cooking_time = int(0)
        self.difficulty = ""

    # all_ingredients class variable
    all_ingredients = []

    # Calculating difficulty of recipes
    def calculate_difficulty(self):
        ingredients_len = len(self.ingredients)

        if self.cooking_time < 10 and ingredients_len < 4:
            self.difficulty = "Easy"
        elif self.cooking_time < 10 and ingredients_len >= 4:
            self.difficulty = "Medium"
        elif self.cooking_time >= 10 and ingredients_len < 4:
            self.difficulty = "Intermediate"
        elif self.cooking_time >= 10 and ingredients_len > 4:
            self.difficulty = "Hard"
        else:
            print("Unable to calculate difficulty")

    # Getter method for name
    def get_name(self):
        return self.name

    # Getter method for cooking_time
    def get_cooking_time(self):
        return self.cooking_time

    # Getter method for ingredients
    def get_ingredients(self):
        return self.ingredients

    # Getter method for difficulty
    def get_difficulty(self):
        if not self.difficulty:
            self.calculate_difficulty()
        return self.difficulty

    # Setter method for name
    def set_name(self, name):
        self.name = name

    # Setter method for cooking_time
    def set_cooking_time(self, cooking_time):
        self.cooking_time = cooking_time

    # Adding ingredients variable
    def add_ingredients(self, items):
        self.ingredients.extend(items)
        self.update_all_ingredients()

    # Search method for ingredient in recipe
    def search_ingredient(self, ingredient):
        return ingredient in self.ingredients

    # Update method for all_ingredients list
    def update_all_ingredients(self):
        for ingredient in self.ingredients:
            if ingredient not in self.all_ingredients:
                self.all_ingredients.append(ingredient)

    # Print recipe
    def __str__(self):
        return f"\n Recipe: {self.name}\n----------------------------\nCooking time (minutes): {self.cooking_time}\nDifficulty: {self.get_difficulty()}\nIngredients:{', '.join(self.ingredients)}"

# Method for recipe search based off of specific ingredient
def recipe_search(data, search_term):
    found = False
    print("\n\nRecipes found with the ingredient:", search_term)
    print("-------------------------------------------")
    for recipe in data:
        if recipe.search_ingredient(search_term):
            print(str(recipe))
            found = True
    if not found:
        print("Could not be found", search_term)

# Main Code

# Tea Recipe
tea = Recipe("Tea")
tea.add_ingredients(["Tea Leaves", "Sugar", "Water"])
tea.set_cooking_time(5)

# Coffee Recipe
coffee = Recipe("Coffee")
coffee.add_ingredients(["Coffee Powder", "Sugar", "Water"])
coffee.set_cooking_time(5)

# Cake Recipe
cake = Recipe("Cake")
cake.add_ingredients(["Sugar", "Butter", "Eggs", "Vanilla Essence", "Flour", "Baking Powder", "Milk"])
cake.set_cooking_time(50)

# Banana Smoothie Recipe
banana_smoothie = Recipe("Banana Smoothie")
banana_smoothie.add_ingredients(["Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes"])
banana_smoothie.set_cooking_time(5)

# Recipe list
recipes_list = [tea, coffee, cake, banana_smoothie]

# Print all recipes
for recipe in recipes_list:
    print (str(recipe))

# Search recipe ingredient (Water, Sugar, Bananas)
recipe_search(recipes_list, "Water")
recipe_search(recipes_list, "Sugar")
recipe_search(recipes_list, "Bananas")