# Imports
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column
from sqlalchemy.types import Integer, String

# Connecting SQLAlchemy with Database
engine = create_engine("mysql://cf-python:password@localhost/task_database")

# Function from SQLAlchemy that generates the declarative base class
Base = declarative_base()

# Creating session
Session = sessionmaker(bind=engine)
session = Session()

# Create table in database
class Recipe(Base):
    __tablename__ = "final_recipes"

    # Define column attributes in table
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))

    # Define __repr__ method
    def __repr__(self):
        return f"<Recipe ID: {self.id}, + Name: {self.name}, Difficulty: {self.difficulty}"
    
    # Define __str__ method
    def __str__(self):
        return (
            f"\nRecipe: {self.name}\n"
            f"{'-' * 25}\n"
            f"Ingredients: {self.ingredients}\n"
            f"Cooking time (in minutes): {self.cooking_time}\n"
            f"Difficulty: {self.difficulty}\n"
        )
    
    # Define method to calculate difficulty
    def calculate_difficulty(self):
        ingredients_len = len(self.ingredients.split(", "))
        self.difficulty = ""
        if self.cooking_time < 10 and ingredients_len < 4:
            self.difficulty = "Easy"
        elif self.cooking_time < 10 and ingredients_len >= 4:
            self.difficulty = "Medium"
        elif self.cooking_time >= 10 and ingredients_len < 4:
            self.difficulty = "Intermediate"
        elif self.cooking_time >= 10 and ingredients_len >= 4:
            self.difficulty = "Hard"
        
    # Define method to retrieve the ingredients string
    def return_ingredients_as_list(self):
        return [] if self.ingredients == "" else self.ingredients.split(", ")

Base.metadata.create_all(engine)

# Menu Class
class Menu(Recipe):
    # Option 1: Create New Recipe
    def create_recipe(self):
        # Recipe name
        name = self.name_input()
        if name is None: return
        
        # Recipe cooking time
        cooking_time = self.cooking_time_input()
        if cooking_time is None: return
        
        # Recipe ingredients
        ingredients = self.ingredients_input()
        if ingredients is None: return

        recipe_entry = Recipe(name=name, ingredients=ingredients, cooking_time=cooking_time)
        recipe_entry.calculate_difficulty()
        session.add(recipe_entry)
        session.commit()
        print("Recipe successfully added.\n")

    # Recipe name input
    def name_input(self):
        name = input("Enter the name of the recipe: ")
        if len(name) > 50:
            print("\nRcipe name must be under 50 characters.\n")
            return None
        elif not name.replace(" ", "").isalnum():
            print("\nInvalid input. Please enter a name containing only letters and numbers.\n")
            return None
        else:
            return name
        
    # Recipe cooking_time input
    def cooking_time_input(self):
        try:
            cooking_time = int(input("Enter the cooking time of the recipe in minutes: "))
            return cooking_time
        except ValueError:
            print("\nThe cooking time needs to be a number.\n")
            return None
    
    # Recipe ingredients input
    def ingredients_input(self):
        ingredients = []
        ingredients_number = input("How many ingredients would you like to enter: ")
        if ingredients_number.isnumeric() == False or int(ingredients_number) <= 0:
            print("\nYou need to enter a positive number.\n")
            return None
        for _ in range(int(ingredients_number)):
            ingredient = input("Enter one ingredient and hit Enter: ")
            if ingredient != "":
                ingredients.append(ingredient)
            else:
                break
        ingredients = ", ".join(ingredients)
        return ingredients

    # Option 2: View All Recipes
    def view_all_recipes(self):
        all_recipes = session.query(Recipe).all()
        if all_recipes:
            for recipe in all_recipes:
                print(recipe)
        else:
            print("\nThere are no recipes yet.\n")

    # Option 3: Search By Ingredients
    def search_by_ingredients(self):
        if session.query(Recipe).count() == 0:
            print("\nThere are no recipes yet.\n")
            return None
        
        results = session.query(Recipe.ingredients).all()
        all_ingredients = []

        for result in results:
            ingredients_list = result[0].split(", ")
            for ingredient in ingredients_list:
                if ingredient not in all_ingredients:
                    all_ingredients.append(ingredient)

        for position, ingredient in enumerate(all_ingredients):
            print("Ingredient " + str(position) + ": " + ingredient)

        try:
            ingredient_indexes = input("Enter the number of the ingredient you would like to search for (space-separated): ").split(" ")
            search_ingredients = []
            for index in ingredient_indexes:
                ingredient_index = int(index)
                search_ingredients.append(all_ingredients[ingredient_index])
        except ValueError:
            print("\nOne or more of your inputs are not numbers.\n")
            return
        except IndexError:
            print("\nThe number you chose does not exist in the list.\n")
            return
        except:
            print("An unexpected error has occurred.\n")
            return
        
        conditions = []
        for search_ingredient in search_ingredients:
            like_term = f"%{search_ingredient}%"
            conditions.append(Recipe.ingredients.like(like_term))
        filtered_recipes = session.query(Recipe).filter(*conditions).all()
        if len(filtered_recipes) <= 0:
            print("\nThere are no recipes containing all of the ingredients.\n")
        else:
            print("\nRecipe(s) containing the ingredient(s):\n")
            for filtered_recipe in filtered_recipes:
                print(filtered_recipe)
    
    # Choose recipe by ID
    def choose_recipe_id(self):
        if session.query(Recipe).count() == 0:
            print("\nThere are no recipes yet.\n")
            return None
        
        results = session.query(Recipe.id, Recipe.name).all()
        recipe_ids = [result[0] for result in results]

        for result in results:
            print("\nRecipe ID:", result[0], "- Recipe Name:", result[1] + "\n")

        try:
            recipe_id = int(input("Enter the id of the recipe you want to choose: "))
        except ValueError:
            print("\nOne or more of your inputs are not in the right format.\n")
            return None
        except:
            print("An unexpected error occurred.\n")
            return
        
        if recipe_id not in recipe_ids:
            print("\nID does not exist.\n")
            return None
        else:
            return recipe_id
            
    # Option 4: Edit A Recipe
    def edit_recipe(self):
        recipe_id = self.choose_recipe_id()
        if recipe_id is None: return

        recipe_to_edit = session.query(Recipe).filter(Recipe.id == recipe_id).one()
        print("Recipe")
        print("-"*10)
        print("1. Name", recipe_to_edit.name)
        print("2. Ingredients:", recipe_to_edit.ingredients)
        print("3. Cooking time:", recipe_to_edit.cooking_time)

        try:
            attribute = int(input("Enther the number of the attribute you would like to update: "))
        except ValueError:
            print("One or more of your inputs are not in the right format.\n")
            return
        except:
            print("\nAn unexpected error occurred.\n")
            return
        
        if attribute == 1:
            name_input = self.name_input()
            if name_input is None: return
            session.query(Recipe).filter(Recipe.id == recipe_id).update({Recipe.name: name_input})
        elif attribute == 2:
            ingredients_input = self.ingredients_input()
            if ingredients_input is None: return
            session.query(Recipe).filter(Recipe.id == recipe_id).update({Recipe.ingredients: ingredients_input})
        elif attribute == 3:
            cooking_time_input = self.cooking_time_input()
            if cooking_time_input is None: return
            session.query(Recipe).filter(Recipe.id == recipe_id).update({Recipe.cooking_time: cooking_time_input})
        else:
            print(f"\nThe number {attribute} was not an option.\n")
            return None

        if attribute == 2 or attribute == 3:
            recipe_to_edit.calculate_difficulty()
        session.commit()
        print("\nRecipe successfully updated.\n")

    # Option 5: Delete Recipe
    def delete_recipe(self):
        recipe_id = self.choose_recipe_id()
        if recipe_id is None: return

        recipe_to_delete = session.query(Recipe).filter(Recipe.id == recipe_id).one()
        decision = input(f"\nAre you sure that you want to delete {recipe_to_delete.name}? Type 'yes': ")

        if decision.lower() == "yes":
            session.delete(recipe_to_delete)
            session.commit()
            print("\nRecipe successfully deleted.\n")
        else:
            print("\nCould not delete recipe.\n")
            return None
    
    # Display Main Menu
    def display_menu(self):
        choice = ""
        while(choice != 'quit'):
            print("Main Menu")
            print("----------")
            print("What would you like to do? Pick a option!")
            print("1. Create a new recipe")
            print("2. View all recipes")
            print("3. Search for recipe by ingredient")
            print("4. Update an existing recipe")
            print("5. Delete a recipe")
            print("Type 'quit' to exit the program.")
            choice = (input("\nYour choice (type in a number or 'quit'): "))

            if choice == "1":
                self.create_recipe()
            elif choice == "2":
                self.view_all_recipes()
            elif choice == "3":
                self.search_by_ingredients()
            elif choice == "4":
                self.edit_recipe()
            elif choice == "5":
                self.delete_recipe()
            elif choice == "quit":
                print("Exiting the program.\n")
                session.close()
                engine.dispose()
                break
            else:
                print("Please write the number of one of the options.\n")

menu = Menu()
menu.display_menu()