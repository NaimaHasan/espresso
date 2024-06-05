"""Recipe Class

This class represents a recipe with its ingredients and instructions.
"""


class Recipe:
    """
    A recipe object containing its details and functionalities.

    Args:
        id (int): The unique identifier of the recipe.
        name (str): The name of the recipe.
        category (str): The category of the recipe (e.g., breakfast, dessert).
        description (str): A description of the recipe.
        ingredients (list): A list of dictionaries representing ingredients.
        steps (list): A list of strings representing the recipe steps.
    """

    def __init__(self, id, name, category, description, ingredients, steps):
        self.id = id
        self.name = name
        self.category = category
        self.description = description
        self.ingredients = ingredients
        self.steps = steps

    def __str__(self):
        return f"Recipe ID: {self.id}, Name: {self.name}, Category: {self.category}"

    def has_ingredients(self, ingredient_names):
        recipe_ingredient_names = set()

        for ingredient in self.ingredients:
            ingredient_name = ingredient['name']
            recipe_ingredient_names.add(ingredient_name.capitalize())

        return recipe_ingredient_names.issuperset(ingredient_names)
