"""Module containing functions for managing ingredients"""

import os

storage_file = "added_ingredients.txt"


def load_added_ingredients():
    if os.path.exists(storage_file):
        with open(storage_file, "r") as file:
            lines = file.readlines()
            added_ingredients = set()

            for line in lines:
                stripped_line = line.strip()
                added_ingredients.add(stripped_line)
            return added_ingredients

    return set()


def save_added_ingredients(added_ingredients):
    with open(storage_file, "w") as file:
        for ingredient in added_ingredients:
            file.write(f"{ingredient}\n")


def find_recipes_by_ingredients(recipes, ingredient_names):
    ingredient_names = {name.lower() for name in ingredient_names}
    searched_recipes = []

    for recipe in recipes:
        if recipe.has_ingredients(ingredient_names):
            searched_recipes.append(recipe)

    return searched_recipes


def display_ingredients(ingredients, added_ingredients):
    print(f"Available Ingredients:")
    for index, ingredient in enumerate(ingredients, start=1):
        print(f"{index}. {ingredient}")

    if added_ingredients:
        print("\nAdded Ingredients:")
        for index, ingredient in enumerate(added_ingredients, start=1):
            print(f"{index}. {ingredient}")
    else:
        print("\nNo ingredients added.")
