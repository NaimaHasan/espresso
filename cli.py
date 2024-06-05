"""Espresso

This Python application helps you manage your coffee ingredients and find recipes based on what you have on hand.
"""

import typer
import services.ingredient_service as ingredient_service
import services.recipe_service as recipe_service
from typing_extensions import Annotated

# Create a Typer application with help message displayed when no arguments provided
app = typer.Typer(no_args_is_help=True)


@app.command()
def find_all_recipes():
    """List all recipes"""
    recipes = recipe_service.load_recipes()
    typer.echo("All Recipes:")
    recipe_service.display_recipe_list(recipes)


@app.command()
def find_recipe_by_id(recipe_id: int):
    """Find a specific recipe by ID"""
    searched_recipe = recipe_service.find_recipe_by_id(recipe_id)

    if searched_recipe:
        recipe_service.display_recipe(searched_recipe)
    else:
        typer.echo(f"Recipe with ID {recipe_id} not found.")


@app.command()
def add_ingredient(ingredient_name: Annotated[str, typer.Option(prompt=True)]):
    """Add ingredients"""
    ingredient_service.add_ingredient(ingredient_name.capitalize())


@app.command()
def remove_ingredient(ingredient_name: Annotated[str, typer.Option(prompt=True)], ):
    """Remove added ingredients"""
    ingredient_service.remove_ingredient(ingredient_name.capitalize())


@app.command()
def clear_ingredients():
    """Clear added ingredients"""
    ingredient_service.clear_ingredients()


@app.command()
def find_recipes_by_added_ingredients():
    """Find recipe by added ingredients"""
    searched_recipes = recipe_service.find_recipes_by_added_ingredients()

    if not searched_recipes:
        typer.echo("No recipes found.")
    else:
        recipe_service.display_recipe_list(searched_recipes)


if __name__ == "__main__":
    app()
