class Recipe:
    def __init__(self, name: str, images: str, ingredients: str, author: str, date: str, rating: str, ingredient_quantities: str, preparation_time: str, instructions: str, category: "Category", id: int, cook_time: str, recipe_yield: str, servings: str, description: str):
        self.__name = name
        self.__images = images
        self.__ingredients = ingredients
        self.__author = author
        self.__date = date
        self.__rating = rating
        self.__ingredient_quantities = ingredient_quantities
        self.__preparation_time = preparation_time
        self.__instructions = instructions
        self.__category = category
        self.__id = id
        self.__cook_time = cook_time
        self.__recipe_yield = recipe_yield
        self.__servings = servings
        self.__description = description
        self.__reviews = []

    def __repr__(self):
        return f"Recipe {self.__name} with id: {self.__id} was created by {self.__date} on {self.__date}"

    @property
    def name(self):
        return self.__name

    @property
    def images(self):
        return self.__images

    @property
    def ingredients(self):
        return self.__ingredients

    @property
    def author(self):
        return self.__author

    @property
    def date(self):
        return self.__date

    @property
    def rating(self):
        return self.__rating

    @property
    def ingredient_quantities(self):
        return self.__ingredient_quantities

    @property
    def preparation_time(self):
        return self.__preparation_time
    @property
    def instructions(self):
        return self.__instructions

    @property
    def category(self):
        return self.__category

    @property
    def id(self):
        return self.__id

    @property
    def cook_time(self):
        return self.__cook_time

    @property
    def recipe_yield(self):
        return self.__recipe_yield

    @property
    def servings(self):
        return self.__servings

    @property
    def description(self):
        return self.__description

    @property
    def reviews(self):
        return self.__reviews
