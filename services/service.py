import requests
from models.recipe import Recipe
from rich.console import Console
from rich.table import Table
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


def load_recipes():
    try:
        response = requests.get(recipe_url)
        response.raise_for_status()
        recipes_data = response.json().get('recipes', [])
        recipes = [create_recipe_from_data(recipe_data) for recipe_data in recipes_data]
        return recipes
    except requests.RequestException as e:
        print(f"Failed to fetch recipes: {e}")
        raise


def create_recipe_from_data(data):
    return Recipe(
        id=data.get('id'),
        name=data.get('name'),
        category=data.get('category'),
        description=data.get('description'),
        ingredients=data.get('ingredients', []),
        steps=data.get('steps', [])
    )


def find_recipes_by_ingredients(recipes, ingredient_names):
    ingredient_names = {name.lower() for name in ingredient_names}
    return [recipe for recipe in recipes if recipe.has_ingredients(ingredient_names)]


def display_recipe(recipe):
    console = Console()

    table = Table("Name", "Description")

    table.add_row("Name", recipe.name)
    table.add_row("Category", recipe.category)
    table.add_row("Description", recipe.description)

    ingredients_str = "\n".join(
        [f"- {ingredient['name']}: {ingredient['quantity']}" for ingredient in recipe.ingredients])
    table.add_row("Ingredients", ingredients_str)

    steps_str = "\n".join([f"{step['number']}. {step['description']}" for step in recipe.steps])
    table.add_row("Steps", steps_str)

    console.print(table)


def display_recipe_list(recipes):
    console = Console()
    table = Table("ID", "Name")

    for recipe in recipes:
        table.add_row(str(recipe.id), recipe.name)

    console.print(table)


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
