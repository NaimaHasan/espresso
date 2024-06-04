"""Module containing functions for managing ingredients"""

import os

recipe_url = "http://naima-hasan-espresso-json.vercel.app/db"
storage_file = "added_ingredients.txt"


def load_added_ingredients():
    if os.path.exists(storage_file):
        with open(storage_file, "r") as file:
            return {line.strip() for line in file.readlines()}
    return set()


def save_added_ingredients(added_ingredients):
    with open(storage_file, "w") as file:
        for ingredient in added_ingredients:
            file.write(f"{ingredient}\n")


def find_recipes_by_ingredients(recipes, ingredient_names):
    ingredient_names = {name.lower() for name in ingredient_names}
    return [recipe for recipe in recipes if recipe.has_ingredients(ingredient_names)]


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
