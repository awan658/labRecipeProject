import csv
from modules.Category import category
from Recipe import recipe

class CSV:
    def __init__(self, filename):
        categories = {}
        category_id = 0
        with open('recipes.csv', 'r') as f:
            csv_file = csv.reader(f)
            for lines in csv_file:
                if lines[10] in categories:
                    categories[lines[10]].add_recipe(
                        Recipe(lines[0], lines[1], lines[2], lines[3], lines[4], lines[5], lines[6], lines[7], lines[8],
                               lines[9], lines[10], lines[11], lines[12], lines[13], lines[14]))
                else:
                    categories[lines[10]] = Category(lines[10], category_id)
                    category_id += 1

    def return_categories(self):
        return categories