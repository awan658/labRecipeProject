from modules.recipe import Recipe
from modules.category import Category

def main():
    categories = []
    categories.append(Category("Pasta", 0))
    categories.append(Category("Rice", 1))

    recipeOne = Recipe(
    name="Spaghetti Carbonara",
    images="https://example.com/images/carbonara.jpg",
    ingredients="Spaghetti, Eggs, Pancetta, Parmesan Cheese, Black Pepper, Salt",
    author="Chef Luigi Rossi",
    date="2025-07-14",
    rating="4.7",
    ingredient_quantities="200g spaghetti, 2 eggs, 100g pancetta, 50g Parmesan, 1 tsp black pepper, salt to taste",
    preparation_time="10 minutes",
    instructions="1. Boil pasta. 2. Fry pancetta. 3. Mix eggs and cheese. 4. Combine all and season.",
    category=Category("Pasta", 0),  # Assuming Category is a class
    id=101,
    cook_time="15 minutes",
    recipe_yield="2 servings",
    servings="2",
    description="A classic Roman pasta dish with creamy eggs, crispy pancetta, and rich Parmesan."
)

    recipeTwo = Recipe(
    name="Creamy Mushroom Fettuccine",
    images="https://example.com/images/mushroom_fettuccine.jpg",
    ingredients="Fettuccine, Mushrooms, Garlic, Heavy Cream, Parmesan, Olive Oil, Parsley, Salt, Pepper",
    author="Isabella Romano",
    date="2025-06-22",
    rating="4.8",
    ingredient_quantities="250g fettuccine, 200g mushrooms, 2 cloves garlic, 150ml heavy cream, 50g Parmesan, 2 tbsp olive oil, chopped parsley, salt and pepper to taste",
    preparation_time="15 minutes",
    instructions=(
        "1. Cook fettuccine until al dente.\n"
        "2. Sauté garlic and mushrooms in olive oil until browned.\n"
        "3. Add cream and simmer for 5 minutes.\n"
        "4. Stir in Parmesan and cooked pasta.\n"
        "5. Garnish with parsley and serve hot."
    ),
    category=Category("Pasta", 0),
    id=102,
    cook_time="20 minutes",
    recipe_yield="2 plates",
    servings="2",
    description="A rich and creamy pasta dish loaded with sautéed mushrooms and finished with Parmesan cheese."
)

    categories[0].add_recipe(recipeOne)
    categories[0].add_recipe(recipeTwo)

    print(recipeOne)
    print(recipeTwo, "\n")

    print(recipeTwo.category)
    print(categories[1], "\n")

    print(categories[0].list_of_recipes(), "\n")

if __name__ == "__main__":
    main()
