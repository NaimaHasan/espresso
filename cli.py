"""Espresso

This Python application helps you manage your coffee ingredients and find recipes based on what you have on hand.
"""

import typer
import services.ingredient_service as ingredient_service
import services.recipe_service as recipe_service
from typing_extensions import Annotated

# Create a Typer application with help message displayed when no arguments provided
app = typer.Typer(no_args_is_help=True)

ingredients = [
    "Espresso",
    "Milk",
    "Caramel",
    "Cream",
    "Sugar"
]

added_ingredients = ingredient_service.load_added_ingredients()


@app.command()
def find_all_recipes():
    """List all recipes"""

    recipes = recipe_service.load_recipes()
    typer.echo("All Recipes:")
    recipe_service.display_recipe_list(recipes)


@app.command()
def find_recipe_by_id(recipe_id: int):
    """Find a specific recipe by ID"""

    recipes = recipe_service.load_recipes()
    found_recipe = None

    for recipe in recipes:
        if recipe.id == recipe_id:
            found_recipe = recipe
            break

    if found_recipe is not None:
        recipe_service.display_recipe(found_recipe)
    else:
        typer.echo(f"Recipe with ID {recipe_id} not found.")


@app.command()
def add_ingredient(ingredient_name: Annotated[str, typer.Option(prompt=True)]):
    """Add ingredients"""

    if ingredient_name.capitalize() in ingredients:
        added_ingredients.add(ingredient_name.capitalize())
    else:
        typer.echo("Ingredient not available\n")

    ingredient_service.save_added_ingredients(added_ingredients)
    ingredient_service.display_ingredients(ingredients, added_ingredients)


@app.command()
def remove_ingredient(ingredient_name: Annotated[str, typer.Option(prompt=True)], ):
    """Remove added ingredients"""

    if ingredient_name.capitalize() in ingredients and ingredient_name.capitalize() in added_ingredients:
        added_ingredients.remove(ingredient_name.capitalize())
        typer.echo(f"Removed ingredient: {ingredient_name.capitalize()}")
    else:
        typer.echo(f"{ingredient_name.capitalize()} is not in the added ingredients.\n")

    ingredient_service.save_added_ingredients(added_ingredients)
    ingredient_service.display_ingredients(ingredients, added_ingredients)


@app.command()
def clear_ingredients():
    """Clear added ingredients"""

    added_ingredients.clear()
    ingredient_service.save_added_ingredients(added_ingredients)
    typer.echo("Added ingredients cleared.")


@app.command()
def find_recipe_by_added_ingredients():
    """Find recipe by added ingredients"""

    recipes = recipe_service.load_recipes()
    searched_recipes = ingredient_service.find_recipes_by_ingredients(recipes, added_ingredients)

    if not searched_recipes:
        print("No recipes found.")
    else:
        recipe_service.display_recipe_list(searched_recipes)


if __name__ == "__main__":
    app()
