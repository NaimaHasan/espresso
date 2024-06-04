import typer
import services.service as service

app = typer.Typer(no_args_is_help=True)

ingredients = [
    "Espresso",
    "Milk",
    "Caramel",
    "Cream",
    "Sugar"
]

added_ingredients = service.load_added_ingredients()


@app.command()
def find_all_recipes():
    """List all recipes"""

    recipes = service.load_recipes()
    typer.echo("All Recipes:")
    service.display_recipe_list(recipes)


@app.command()
def find_recipe_by_id(recipe_id: int):
    """Find a specific recipe by ID"""

    recipes = service.load_recipes()

    recipe = next((recipe for recipe in recipes if recipe.id == recipe_id), None)

    if recipe is not None:
        service.display_recipe(recipe)
    else:
        typer.echo(f"Recipe with ID {recipe_id} not found.")


@app.command()
def add_ingredients(espresso: bool = typer.Option(False, "--espresso", help="Add Espresso"),
                    milk: bool = typer.Option(False, "--milk", help="Add Milk"),
                    caramel: bool = typer.Option(False, "--caramel", help="Add Caramel"),
                    cream: bool = typer.Option(False, "--cream", help="Add Cream"),
                    sugar: bool = typer.Option(False, "--sugar", help="Add Sugar")):
    """Add ingredients"""

    for option in ingredients:
        if vars()[option.lower()]:
            added_ingredients.add(option)

    service.save_added_ingredients(added_ingredients)
    service.display_ingredients(ingredients, added_ingredients)


@app.command()
def remove_ingredients(espresso: bool = typer.Option(False, "--espresso", help="Remove Espresso"),
                       milk: bool = typer.Option(False, "--milk", help="Remove Milk"),
                       caramel: bool = typer.Option(False, "--caramel", help="Remove Caramel"),
                       cream: bool = typer.Option(False, "--cream", help="Remove Cream"),
                       sugar: bool = typer.Option(False, "--sugar", help="Remove Sugar")):
    """Remove added ingredients"""

    for option in ingredients:
        if vars()[option.lower()]:
            if option in added_ingredients:
                added_ingredients.remove(option)
                typer.echo(f"Removed ingredient: {option}")
            else:
                typer.echo(f"{option} is not in the added ingredients.")

    service.save_added_ingredients(added_ingredients)
    service.display_ingredients(ingredients, added_ingredients)


@app.command()
def clear_ingredients():
    """Clear added ingredients"""

    added_ingredients.clear()
    service.save_added_ingredients(added_ingredients)
    typer.echo("Added ingredients cleared.")


@app.command()
def find_recipe_by_added_ingredients():
    """Find recipe by added ingredients"""

    recipes = service.load_recipes()
    searched_recipes = service.find_recipes_by_ingredients(recipes, added_ingredients)

    if not searched_recipes:
        print("No recipes found.")
    else:
        service.display_recipe_list(searched_recipes)


if __name__ == "__main__":
    app()
