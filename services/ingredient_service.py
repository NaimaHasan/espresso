"""Module containing functions for managing ingredients"""

import os
import typer

ingredients = [
    "Espresso",
    "Milk",
    "Caramel",
    "Cream",
    "Sugar"
]

storage_file = "added_ingredients.txt"


def add_ingredient(ingredient):
    added_ingredients = load_added_ingredients()

    if ingredient in ingredients:
        if ingredient not in added_ingredients:
            added_ingredients.add(ingredient)
            save_added_ingredients(added_ingredients)
    else:
        typer.echo("Ingredient not available\n")

    display_ingredients()


def remove_ingredient(ingredient):
    added_ingredients = load_added_ingredients()

    if ingredient in ingredients and ingredient in added_ingredients:
        added_ingredients.remove(ingredient)
        save_added_ingredients(added_ingredients)
        typer.echo(f"Removed ingredient: {ingredient}")
    else:
        typer.echo(f"{ingredient} is not in the added ingredients.\n")

    display_ingredients()


def clear_ingredients():
    added_ingredients = load_added_ingredients()

    added_ingredients.clear()
    save_added_ingredients(added_ingredients)
    typer.echo("Added ingredients cleared.")


def load_added_ingredients():
    added_ingredients = set()

    if os.path.exists(storage_file):
        with open(storage_file, "r") as file:
            lines = file.readlines()

            for line in lines:
                stripped_line = line.strip()
                added_ingredients.add(stripped_line)
            return added_ingredients

    return added_ingredients


def save_added_ingredients(added_ingredients):
    with open(storage_file, "w") as file:
        for ingredient in added_ingredients:
            file.write(f"{ingredient}\n")


def display_ingredients():
    added_ingredients = load_added_ingredients()

    typer.echo(f"Available Ingredients:")
    for index, ingredient in enumerate(ingredients, start=1):
        typer.echo(f"{index}. {ingredient}")

    if added_ingredients:
        typer.echo("\nAdded Ingredients:")
        for index, ingredient in enumerate(added_ingredients, start=1):
            typer.echo(f"{index}. {ingredient}")
    else:
        typer.echo("\nNo ingredients added.")
