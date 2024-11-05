## Espresso: Coffee Ingredient Management and Recipe Discovery

A Python CLI application to discover coffee recipes based on what ingredients you have available.

### Features

* **Ingredient Management:**
  * Add, remove, and clear ingredients.
  * Keep track of your coffee supplies.
* **Recipe Exploration:**
  * List all available coffee recipes.
  * Find a specific recipe by its ID.
  * Discover recipes you can make with your current ingredients.

### Usage

This application uses the Typer library for a user-friendly command-line interface.

**1. Setting Up Your Development Environment:**

Before starting, ensure you have Python installed. You can then create a virtual environment and install dependencies from the `requirements.txt` file:

**a. Create a virtual environment (recommended):**

- Isolates project dependencies and avoids conflicts with system-wide Python installations.

**Windows:**

```bash
py -m venv <venv_name>
```

**macOS/Linux:**

```bash
python3 -m venv <venv_name>
```

Replace `<venv_name>` with your desired name (e.g., `espresso_env`).

**b. Activate the virtual environment:**

**Windows:**

```bash
<venv_name>\Scripts\activate.bat
```

**macOS/Linux:**

```bash
source <venv_name>/bin/activate
```

**c. Install dependencies:**

Within the activated virtual environment, run:

```bash
pip install -r requirements.txt
```

This command reads the `requirements.txt` file and installs all specified dependencies.

**2. Run the Application:**

Navigate to the directory containing the `cli.py` file and run:

```bash
python cli.py
```

This will display the help message with available commands.

**3. Available Commands:**

* `find_all_recipes`: Lists all available coffee recipes.
* `find_recipe_by_id <recipe_id>`: Finds a specific recipe by its ID.
* `add_ingredients`: Adds selected ingredients to your inventory.
* `remove_ingredients`: Removes selected ingredients from your inventory.
* `clear_ingredients`: Clears all added ingredients from your inventory.
* `find_recipe_by_added_ingredients`: Discovers recipes you can create based on your current inventory.

**4. Services:**

This application utilizes two services:

* `ingredient_service`: Handles loading, saving, and managing the list of added ingredients.
* `recipe_service`: Handles loading, displaying, and searching for recipes.

**Feel free to contribute or raise issues on this repository!**
