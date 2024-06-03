import requests
from models.recipe import Recipe

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


def find_recipes_by_ingredients(recipes, ingredient_names):
    ingredient_names = {name.lower() for name in ingredient_names}
    return [recipe for recipe in recipes if recipe.has_ingredients(ingredient_names)]
