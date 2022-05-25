from pprint import pprint


def open_recipe_book(file):
    with open(file, encoding='utf-8') as recipe:
        recipe_book = {}
        for line in recipe:
            dish = line.strip()
            quantity = int(recipe.readline().strip())
            result = []
            for item in range(quantity):
                data = {}
                string = recipe.readline().split('|')
                data['ingredient_name'] = string[0].strip()
                data['quantity'] = int(string[1].strip())
                data['measure'] = string[2].strip()
                result.append(data)
            recipe_book[dish] = result
            recipe.readline()
    return recipe_book


def get_shop_list_by_dishes(dishes, recipe_book, person_count=1):
    tmp = []
    for dish in dishes:
        if dish in recipe_book.keys():
            tmp.append(recipe_book[dish])
    tmp1 = []
    for item in tmp:
        for i in range(len(item)):
            tmp1.append(item[i])
    result = {}
    for item in tmp1:
        tmp2 = dict()
        tmp2['measure'] = item['measure']
        if item['ingredient_name'] not in result.keys():
            tmp2['quantity'] = item['quantity']*person_count
        else:
            tmp2['quantity'] = (result[item['ingredient_name']]['quantity'] + item['quantity']*person_count)
        result[item['ingredient_name']] = tmp2
    return result


file = 'recipe.txt'
recipe_book = open_recipe_book(file)
list_of_ingredients = get_shop_list_by_dishes(['Омлет', 'Омлет', 'Омлет', 'Фахитос'], recipe_book, 2)
pprint(list_of_ingredients)



