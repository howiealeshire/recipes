
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


def load_keys_to_replace():
    lines = []
    with open('keys_to_merge.txt') as f:
        lines = f.read().splitlines()
    mega_list = []
    for elem in lines:
        mega_list.append(elem.split(','))
    mega_list2 = []
    for elem in mega_list:
        elem2 = list(map(str.strip,elem))
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
        elem_l = list(map(str.lower,elem_l))
        if first_elem == j:
            first_elem = 'jalapeño'
        first_elem = first_elem.lower()
        temp_dict = {first_elem:elem_l}
        l_dict.append(temp_dict)
    pprint(l_dict)

# Function to replace values in a cell with dictionary keys

ingredients_key = 'Ingredients'


def replace_with_key(cell_value):
    for item in replacement_dict:
        for key, values in item.items():
            if cell_value in values:
                return key
    return cell_value


if __name__ == "__main__":
    # Normalize
    load_keys_to_replace()
    df = pd.read_excel('Recipes.xlsx')
    df.to_json('recipes.json')
    ingredients = df[ingredients_key].values
    df[ingredients_key] = df[ingredients_key].apply(str.strip)
    df[ingredients_key] = df[ingredients_key].apply(replace_with_key)





