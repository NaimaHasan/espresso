"""Module containing functions for managing recipes."""

import requests
import typer

from models.recipe import Recipe
from rich.console import Console
from rich.table import Table

from services import ingredient_service

recipe_url = "http://naima-hasan-espresso-json.vercel.app/db"


def load_recipes():
    try:
        response = requests.get(recipe_url)
        response.raise_for_status()
        recipes_data = response.json().get('recipes', [])

        recipes = [create_recipe_from_data(recipe_data) for recipe_data in recipes_data]
        return recipes

    except requests.RequestException as e:
        typer.echo(f"Failed to fetch recipes: {e}")
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
    ingredients_str = convert_ingredient_to_string(recipe.ingredients)
    steps_str = convert_steps_to_string(recipe.steps)

    fields = [
        ("Name", recipe.name),
        ("Category", recipe.category),
        ("Description", recipe.description),
        ("Ingredients", ingredients_str),
        ("Steps", steps_str),
    ]

    console = Console()

    table = Table("Name", "Description")

    for field_name, field_value in fields:
        table.add_row(field_name, field_value)

    console.print(table)


def convert_ingredient_to_string(ingredients):
    ingredients_list = []

    for ingredient in ingredients:
        ingredient_str = f"- {ingredient['name']}: {ingredient['quantity']}"
        ingredients_list.append(ingredient_str)

    ingredients_str = "\n".join(ingredients_list)

    return ingredients_str


def convert_steps_to_string(steps):
    step_list = []

    for step in steps:
        step_str = f"{step['number']}. {step['description']}"
        step_list.append(step_str)

    steps_str = "\n".join(step_list)

    return steps_str


def display_recipe_list(recipes):
    console = Console()
    table = Table("ID", "Name")

    for recipe in recipes:
        table.add_row(str(recipe.id), recipe.name)

    console.print(table)


def find_recipe_by_id(recipe_id):
    recipes = load_recipes()

    for recipe in recipes:
        if recipe.id == recipe_id:
            return recipe


def find_recipes_by_added_ingredients():
    recipes = load_recipes()
    added_ingredients = ingredient_service.load_added_ingredients()
    searched_recipes = []

    for recipe in recipes:
        if recipe.has_ingredients(added_ingredients):
            searched_recipes.append(recipe)

    return searched_recipes
