import typer
import os
from rich.console import Console
from rich.table import Table

from services.service import load_recipes, find_recipes_by_ingredients

app = typer.Typer(no_args_is_help=True)

ingredients = [
    "Espresso",
    "Milk",
    "Caramel",
    "Cream",
    "Sugar"
]

storage_file = "added_ingredients.txt"


def bold(text: str) -> str:
    return f"\033[1m{text}\033[0m"


def load_added_ingredients():
    if os.path.exists(storage_file):
        with open(storage_file, "r") as file:
            return {line.strip() for line in file.readlines()}
    return set()


added_ingredients = load_added_ingredients()


@app.command()
def add_ingredients(espresso: bool = typer.Option(False, "--espresso", help="Add Espresso"),
                    milk: bool = typer.Option(False, "--milk", help="Add Milk"),
                    caramel: bool = typer.Option(False, "--caramel", help="Add Caramel"),
                    cream: bool = typer.Option(False, "--cream", help="Add Cream"),
                    sugar: bool = typer.Option(False, "--sugar", help="Add Sugar")):
    """Add ingredients"""
    options = ["espresso", "milk", "caramel", "cream", "sugar"]

    for option in options:
        if vars()[option]:
            added_ingredients.add(option.capitalize())

    save_added_ingredients(added_ingredients)
    show_ingredients()


@app.command()
def remove_ingredients(espresso: bool = typer.Option(False, "--espresso", help="Remove Espresso"),
                       milk: bool = typer.Option(False, "--milk", help="Remove Milk"),
                       caramel: bool = typer.Option(False, "--caramel", help="Remove Caramel"),
                       cream: bool = typer.Option(False, "--cream", help="Remove Cream"),
                       sugar: bool = typer.Option(False, "--sugar", help="Remove Sugar")):
    """Remove added ingredients"""
    options = ["espresso", "milk", "caramel", "cream", "sugar"]

    for option in options:
        if vars()[option]:
            if option.capitalize() in added_ingredients:
                added_ingredients.remove(option.capitalize())
                typer.echo(f"Removed ingredient: {option.capitalize()}")
            else:
                typer.echo(f"{option.capitalize()} is not in the added ingredients.")

    save_added_ingredients(added_ingredients)
    show_ingredients()


@app.command()
def clear_ingredients():
    """Clear added ingredients"""
    added_ingredients.clear()
    save_added_ingredients(added_ingredients)
    typer.echo("Added ingredients cleared.")


def save_added_ingredients(added_ingredients):
    with open(storage_file, "w") as file:
        for ingredient in added_ingredients:
            file.write(f"{ingredient}\n")


def show_ingredients():
    print(f"Available Ingredients:")
    for index, ingredient in enumerate(ingredients, start=1):
        print(f"{index}. {ingredient}")

    if added_ingredients:
        print("\nAdded Ingredients:")
        for index, ingredient in enumerate(added_ingredients, start=1):
            print(f"{index}. {ingredient}")
    else:
        print("\nNo ingredients added.")


@app.command()
def find_recipe_by_added_ingredients():
    """Find recipe by added ingredients"""
    recipes = load_recipes()
    searched_recipes = find_recipes_by_ingredients(recipes, added_ingredients)
    display_recipes(searched_recipes)


@app.command()
def find_all_recipes():
    """List all recipes"""
    recipes = load_recipes()
    typer.echo("All Recipes:")
    display_recipes(recipes)


def display_recipes(recipes):
    console = Console()
    table = Table("ID", "Name")

    for recipe in recipes:
        table.add_row(str(recipe.id), recipe.name)

    console.print(table)


@app.command()
def find_recipe_by_id(recipe_id: int):
    """Find a specific recipe by ID"""
    recipes = load_recipes()

    for recipe in recipes:
        if recipe.id == recipe_id:
            display_recipe(recipe)


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


if __name__ == "__main__":
    app()
