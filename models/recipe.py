class Recipe:
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
        recipe_ingredient_names = {ingredient['name'].lower() for ingredient in self.ingredients}
        return recipe_ingredient_names.issuperset(ingredient_names)