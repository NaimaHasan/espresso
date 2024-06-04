"""Module containing functions for managing recipes."""

import requests
from models.recipe import Recipe
from rich.console import Console
from rich.table import Table

recipe_url = "http://naima-hasan-espresso-json.vercel.app/db"


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



