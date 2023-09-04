import pandas as pd
from pprint import pprint

replacement_dict = [{'chilies': ['green chilies', 'green chili', 'green chilis']},
                    {'canned tomatoes': ['tomatoes']},
                    {'ginger': ['ginger']},
                    {'grated': ['grated cheese', 'cheese']},
                    {'green bell pepper': ['bell pepper']},
                    {'jalapeño': ['jalapeños']},
                    {'black pepper': ['pepper']},
                    {'grits': ['polenta']},
                    {'potato': ['russet potato']},
                    {'soy sauce': ['soy sauce']}]

price_mappings_non_normalized = {'anchovy': '1.38',
                                 'baking powder': '0.65',
                                 'baking soda': '0.08',
                                 'banana': '0.69/lb',
                                 'basil': '4.38',
                                 'bay leaf': '51.06',
                                 'beans': '0.10',
                                 'beef chuck': '9.39/lb',
                                 'bell pepper': '2.75/lb',
                                 'black pepper': '1.89',
                                 'bread': '0.10',
                                 'broccoli rabe': '4.41',
                                 'brown sugar': '0.11',
                                 'brussels sprout': '4.41/lb',
                                 'bun': '0.25/count',
                                 'butter': '0.68',
                                 'canned tomato': '0.08',
                                 'canned tomatoes': '0.08',
                                 'carrot': '1.43/lb',
                                 'cauliflower': '4.41/ct',
                                 'cayenne': '3.31',
                                 'celery': '0.41',
                                 'cheese': '0.41',
                                 'chicken stock': '0.10',
                                 'chicken thigh': '4.97/lb',
                                 'chickpeas': '0.08',
                                 'chili flakes': '1.46',
                                 'chilies': '0.47',
                                 'cilantro': '1.65/ct',
                                 'coriander': '1.35',
                                 'cornstarch': '0.17',
                                 'cream': '0.44',
                                 'cucumber': '0.83/ct',
                                 'cumin': '1.32',
                                 'dijon mustard': '0.22',
                                 'dill': '4.74',
                                 'dried spaghetti': '0.13',
                                 'egg': '0.18',
                                 'egg noodles': '0.33',
                                 'eggplant': '2.75/lb',
                                 'fettuccine': '0.09',
                                 'flour': '0.07',
                                 'fresh mozzarella': '0.69',
                                 'fresh spinach': '0.3',
                                 'garam masala': '2.92',
                                 'garlic': '5.53/lb',
                                 'garlic powder': '0.71',
                                 'ginger': '5.53/lb',
                                 'ginger ': '5.53/lb',
                                 'grated': '0.41',
                                 'grated cheese': '0.41',
                                 'green bell pepper': '2.75/lb',
                                 'green chili': '0.47',
                                 'green chilis': '0.47',
                                 'grits': '0.19',
                                 'ground beef': '0.38',
                                 'instant yeast': '7.48',
                                 'jalapeã±o ': '5.53/lb',
                                 'jalapeã±os ': '5.53/lb',
                                 'jam': '0.22',
                                 'kale': '1.83/lb',
                                 'leek': '2.19/ct',
                                 'lemon': '1.09/ct',
                                 'lemon juice': '0.15/oz',
                                 'milk': '0.03',
                                 'mushroom': '0.30',
                                 'mustard': '0.22',
                                 'olive': '0.46',
                                 'olive oil': '0.49',
                                 'onion': '2.19/lb',
                                 'oregano': '1.22',
                                 'paprika': '1.03',
                                 'peanut butter': '0.17',
                                 'pepper': '1.89',
                                 'polenta': '0.20',
                                 'potato': '0.95/lb',
                                 'red onion': '2.03/lb',
                                 'rice': '0.11',
                                 'rice vinegar ': '0.28',
                                 'rigatoni': '0.13',
                                 'rolled oats': '0.15',
                                 'russet potato': '0.95/lb',
                                 'salsa': '0.17',
                                 'salt': '0.05',
                                 'scallion': '1.05/ct',
                                 'shrimp': '0.83',
                                 'smoked paprika': '1.22',
                                 'sour cream': '0.21',
                                 'soy sauce': '0.22',
                                 'soy sauce ': '0.22',
                                 'tahini': '0.48',
                                 'thyme': '5.16',
                                 'tomato': '1.65/lb',
                                 'tortilla': '0.02',
                                 'turmeric': '2.93',
                                 'vanilla': '3.32',
                                 'vegetable oil': '0.16',
                                 'yogurt': '0.16',
                                 'zucchini': '1.77/lb'}

conversion_factors = {
    'clove': 0.11,  # Example conversion factor for 'clove'
    'count': 1,  # Default conversion factor for 'count'
    'cup': 8,  # Conversion factor for 'cup'
    'cups': 8,  # Conversion factor for 'cups'
    'head': 19,  # Conversion factor for 'head'
    'lb': 16,  # Conversion factor for 'lb'
    'oz': 1,  # Conversion factor for 'oz'
    'slice': 1,  # Custom conversion factor for 'slice'
    'tbsp': 0.5,  # Conversion factor for 'tbsp'
    'tsp': 0.1667  # Conversion factor for 'tsp'
}

counts_dict = {'anchovy': 2,
               'banana': 4.16,
               'bay leaf': 0.0071,
               'broccoli rabe': 1.41,
               'bun': 2,
               'carrot': 2.12,
               'celery': 2.26,
               'chicken thigh': 4,
               'chilies': 1.6,
               'cucumber': 5.3,
               'egg': 1.7,
               'eggplant': 19,
               'green bell pepper': 4.5,
               'jalapeño': 0.5,
               'kale': 2,
               'leek': 7.05,
               'lemon': 3,
               'olive': 0.11,
               'onion': 6,
               'potato': 8,
               'rice': 0.002,
               'scallion': 0.53,
               'tomato': 4,
               'tortilla': 1.06,
               'zucchini': 6.9137}

measurement_key = 'Measurement'

price_mappings_in_oz = {'anchovy': 1.38,
                        'baking powder': 0.65,
                        'baking soda': 0.08,
                        'banana': 11.04,
                        'basil': 4.38,
                        'bay leaf': 51.06,
                        'beans': 0.1,
                        'beef chuck': 150.24,
                        'bell pepper': 44.0,
                        'black pepper': 1.89,
                        'bread': 0.1,
                        'broccoli rabe': 4.41,
                        'brown sugar': 0.11,
                        'brussels sprout': 70.56,
                        'bun': 0.25,
                        'butter': 0.68,
                        'canned tomato': 0.08,
                        'canned tomatoes': 0.08,
                        'carrot': 22.88,
                        'cayenne': 3.31,
                        'celery': 0.41,
                        'cheese': 0.41,
                        'chicken stock': 0.1,
                        'chicken thigh': 79.52,
                        'chickpeas': 0.08,
                        'chili flakes': 1.46,
                        'chilies': 0.47,
                        'coriander': 1.35,
                        'cornstarch': 0.17,
                        'cream': 0.44,
                        'cucumber': 4.399,
                        'cumin': 1.32,
                        'dijon mustard': 0.22,
                        'dill': 4.74,
                        'dried spaghetti': 0.13,
                        'egg': 0.18,
                        'egg noodles': 0.33,
                        'eggplant': 44.0,
                        'fettuccine': 0.09,
                        'flour': 0.07,
                        'fresh mozzarella': 0.69,
                        'fresh spinach': 0.3,
                        'garam masala': 2.92,
                        'garlic': 88.48,
                        'garlic powder': 0.71,
                        'ginger': 88.48,
                        'ginger ': 88.48,
                        'grated': 0.41,
                        'grated cheese': 0.41,
                        'green bell pepper': 44.0,
                        'green chili': 0.47,
                        'green chilis': 0.47,
                        'grits': 0.19,
                        'ground beef': 0.38,
                        'instant yeast': 7.48,
                        'jalapeño ': 88.48,
                        'jalapeños': 88.48,
                        'jam': 0.22,
                        'kale': 29.28,
                        'leek': 15.439499999999999,
                        'lemon': 3.2700000000000005,
                        'lemon juice': 0.15,
                        'milk': 0.03,
                        'mushroom': 0.3,
                        'mustard': 0.22,
                        'olive': 0.46,
                        'olive oil': 0.49,
                        'onion': 35.04,
                        'oregano': 1.22,
                        'paprika': 1.03,
                        'peanut butter': 0.17,
                        'pepper': 1.89,
                        'polenta': 0.2,
                        'potato': 15.2,
                        'red onion': 32.48,
                        'rice': 0.11,
                        'rice vinegar': 0.28,
                        'rigatoni': 0.13,
                        'rolled oats': 0.15,
                        'russet potato': 15.2,
                        'salsa': 0.17,
                        'salt': 0.05,
                        'scallion': 0.5565000000000001,
                        'shrimp': 0.83,
                        'smoked paprika': 1.22,
                        'sour cream': 0.21,
                        'soy sauce': 0.22,
                        'tahini': 0.48,
                        'thyme': 5.16,
                        'tomato': 26.4,
                        'tortilla': 0.02,
                        'turmeric': 2.93,
                        'vanilla': 3.32,
                        'vegetable oil': 0.16,
                        'yogurt': 0.16,
                        'zucchini': 28.32}


# Function to convert quantities to ounces and apply custom mappings
def convert_to_oz(row):
    quantity, measurement = row['Quantity'], row[measurement_key]
    # Use the conversion factor from the dictionary, defaulting to 1 if not found
    conversion_factor = conversion_factors.get(measurement, 1)
    return quantity * conversion_factor


def load_keys_to_replace():
    lines = []
    with open('keys_to_merge.txt') as f:
        lines = f.read().splitlines()
    mega_list = []
    for elem in lines:
        mega_list.append(elem.split(','))
    mega_list2 = []
    for elem in mega_list:
        elem2 = list(map(str.strip, elem))
        mega_list2.append(elem2)
    l_dict = []
    j = 'JalapeÃ±o'
    j2 = 'JalapeÃ±os'
    for elem in mega_list2:
        elem_l = elem
        first_elem = elem_l[0]
        elem_l.pop(0)
        elem_l = [x for x in elem_l if x]
        if elem_l[0] == j2:
            elem_l[0] = 'jalapeños'
        elem_l = list(map(str.lower, elem_l))
        if first_elem == j:
            first_elem = 'jalapeño'
        first_elem = first_elem.lower()
        temp_dict = {first_elem: elem_l}
        l_dict.append(temp_dict)
    # pprint(l_dict)


# Function to replace values in a cell with dictionary keys

ingredients_key = 'Ingredients'


def get_new_price_mappings():
    # Initialize a new dictionary for price mappings with converted values
    price_mappings_converted = {}

    # Iterate over the price_mappings_non_normalized dictionary
    for ingredient, price_str in price_mappings_non_normalized.items():
        # Split the price string into the value and measurement
        try:
            value_str, measurement_str = price_str.split('/')
        except ValueError as e:
            price_mappings_converted[ingredient] = float(price_str)
            continue
        # Handle different measurement units
        if measurement_str == 'oz':
            # No conversion needed for 'oz'
            price_mappings_converted[ingredient] = float(value_str)
        elif measurement_str == 'ct':
            # Convert count to oz using counts_dict
            if ingredient in counts_dict:
                price_mappings_converted[ingredient] = float(value_str) * counts_dict[ingredient]
        else:
            # Convert other measurements to oz using conversion_factors
            if measurement_str in conversion_factors:
                price_mappings_converted[ingredient] = float(value_str) * conversion_factors[measurement_str]

    pprint(price_mappings_converted)
    # # Print the resulting new dictionary
    # for ingredient, price in price_mappings_converted.items():
    #     print(f'{ingredient}: {price:.2f} oz')


def new_func(elem):
    elem = elem.strip()
    return elem.strip("'")


# Function to replace 'Quantity' based on 'Ingredients' using the dictionary
# Function to multiply 'Quantity' by the value from 'counts_dict' based on 'Ingredients'
def multiply_quantity(row):
    ingredient = row['Ingredients']
    if ingredient in counts_dict:
        return row['Quantity'] * counts_dict[ingredient]
    return row['Quantity']


def get_price_mappings():
    with open('recipe_price_mappings.txt') as f:
        lines = f.read().splitlines()
    lines = [x for x in lines if x]
    lines = list(map(str.lower, lines))
    lines = list(map(str.strip, lines))
    mega_list = []
    for elem in lines:
        mega_list.append(elem.split(','))
    mega_list2 = []
    for elem in mega_list:
        lines = list(map(new_func, elem))
        lines = [x for x in lines if x]
        # lines.pop(elem.index('vegetable'))
        mega_list2.append(lines)

    pprint(mega_list2)


def replace_with_key(cell_value):
    for item in replacement_dict:
        for key, values in item.items():
            if cell_value in values:
                return key
    return cell_value


# def normalize_price_mappings():
#     d = []
#     for elem in price_mappings_list_non_normalized:
#         d.append({elem[0]: elem[1]})
#     pprint(d)

# Function to calculate 'Normalized Prices' with error handling
def calculate_normalized_prices(row):
    ingredient = row[ingredients_key]
    try:
        price_per_oz = price_mappings_in_oz[ingredient]
        return row['Normalized count'] * price_per_oz
    except KeyError:
        return None  # Return None for missing ingredients

serving_size_key = 'Serving Size'
quantity_key = 'Quantity'

if __name__ == "__main__":
    df = pd.read_excel('Recipes_normalized_partially2.xlsx')



def main():
    # Normalize
    load_keys_to_replace()
    df = pd.read_excel('Recipes.xlsx')
    # df.to_json('recipes.json')
    ingredients = df[ingredients_key].values
    df[ingredients_key] = df[ingredients_key].apply(str.strip)
    df[ingredients_key] = df[ingredients_key].apply(replace_with_key)
    # pprint(df[quantity_key])
    # pprint(set(df[measurement_key].dropna()))
    # get_price_mappings()
    # normalize_price_mappings()
    df['Normalized count'] = df.apply(convert_to_oz, axis=1)
    # print(df['Normalized count'])
    df[measurement_key] = df[measurement_key].fillna('')
    df[measurement_key] = df[measurement_key].str.replace(r'\bount\b', 'count', regex=True)
    df['Quantity'] = df.apply(multiply_quantity, axis=1)
    # filtered_entries = df[df[measurement_key].str.contains('count')]
    # df.to_excel('Recipes_normalized_partially.xlsx')
    # Print the filtered entries
    # print(filtered_entries[measurement_key])
    # print(filtered_entries[ingredients_key])
    # get_new_price_mappings()
    df = pd.read_excel('Recipes_normalized_partially_further.xlsx')
    # Add a new column 'Normalized Prices' using the function
    df['Normalized Prices'] = df.apply(calculate_normalized_prices, axis=1)

    df.to_excel('Recipes_normalized_partially2.xlsx')
