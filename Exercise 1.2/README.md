# Create a structure for `recipes_1` (sequential change to the #)
- **name (str):** Contains the name of the recipe.
- **cooking_time (int):** Contains the cooking time in minutes.
- **ingredients (list):** Contains a number of ingredients, each of the str data type.

I opted to utilize the dictionary data type for `recipe_1`. This choice is ideal because dictionaries enable storage of data in key-value pairs, which aligns well with representing the diverse properties of a recipe. Moreover, dictionaries can accommodate various data types, essential for managing different types of information in a recipe, such as lists for ingredients and integers for cooking times.

# Outer structure (all_recipes)
- I chose to use a list for `all_recipes` because lists can store multiple items or recipes. Lists are also mutable, which means recipes can be added to or removed from `all_recipes` easily when needed.