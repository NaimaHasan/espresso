## Espresso

This Python application helps you manage your coffee ingredients and find recipes based on what you have on hand.

### Features

* List all available coffee recipes
* Find a specific recipe by ID
* Add ingredients to your inventory
* Remove ingredients from your inventory
* Clear all added ingredients
* Find recipes that you can make with your current ingredients

### Usage

This application uses the Typer library for a command-line interface.

**1. Install dependencies**

Make sure you have Python and Typer installed. You can install Typer using pip:

```bash
pip install typer
```

**2. Run the application**

Navigate to the directory containing this file and run:

```bash
python cli.py
```

This will display the help message with all available commands.

**3. Available commands**

* `find_all_recipes`: Lists all available coffee recipes.
* `find_recipe_by_id <recipe_id>`: Finds a specific recipe by its ID.
* `add_ingredients [--espresso] [--milk] [--caramel] [--cream] [--sugar]`: Adds selected ingredients to your inventory.
* `remove_ingredients [--espresso] [--milk] [--caramel] [--cream] [--sugar]`: Removes selected ingredients from your inventory.
* `clear_ingredients`: Clears all added ingredients from your inventory.
* `find_recipe_by_added_ingredients`: Finds recipes that you can make with your current ingredients.

**4. Services**

This application utilizes two services:

* `ingredient_service`: Handles loading, saving, and managing the list of added ingredients.
* `recipe_service`: Handles loading, displaying, and searching for recipes.

