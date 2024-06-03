import typer
import os
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


# Global variable to store added ingredients
added_ingredients = load_added_ingredients()


@app.command()
def add_ingredients(espresso: bool = typer.Option(False, "--espresso", help="Add Espresso"),
                    milk: bool = typer.Option(False, "--milk", help="Add Milk"),
                    caramel: bool = typer.Option(False, "--caramel", help="Add Caramel"),
                    cream: bool = typer.Option(False, "--cream", help="Add Cream"),
                    sugar: bool = typer.Option(False, "--sugar", help="Add Sugar")):
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
    recipes = load_recipes()
    searched_recipes = find_recipes_by_ingredients(recipes, added_ingredients)
    for recipe in searched_recipes:
        typer.echo(f"ID: {recipe.id} Name: {recipe.name}")


@app.command()
def show_all_recipes():
    """List all recipes"""
    recipes = load_recipes()
    typer.echo("All Recipes:")
    for recipe in recipes:
        typer.echo(f"ID: {recipe.id} Name: {recipe.name}")


@app.command()
def view_recipe_by_id(recipe_id: int):
    """View a specific recipe by ID"""
    recipes = load_recipes()
    display_recipe(recipe_id, recipes)


def display_recipe(recipe_id, recipes):
    for recipe in recipes:
        if recipe.id == recipe_id:
            print(f"{bold('Recipe Name')}: {recipe.name}\n")

            print(f"{bold('Category')}: {recipe.category}\n")

            print(f"{bold('Description')}: {recipe.description}\n")

            print(f"{bold('Ingredients')}:")
            for ingredient in recipe.ingredients:
                print(f"- {ingredient['name']}: {ingredient['quantity']}")

            print(f"\n{bold('Steps')}:")
            for step in recipe.steps:
                print(f"{step['number']}. {step['description']}\n")
            return

    print("Recipe not found.")


if __name__ == "__main__":
    app()
