class Category:
    def __init__(self, name: str, id: int):
        self.__name = name
        self.__id = id
        self.__recipes = []

    def __repr__(self):
        return f"Category {self.__id}: {self.__name}"

    def add_recipe(self, recipe: "Recipe"):
        self.__recipes.append(recipe)

    def list_of_recipes(self):
        return f"Category {self.__name} has the following associated recipes: {self.__recipes}"