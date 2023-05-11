source_dict = {"Cook Book": [
    {"Dish A": ["oil", "bacon", "oil"]},
    {"Dish B": ["eggs", "oil", "eggs"]},
    {"Dish B": ["bacon", "oil", "bacon"]}
]}


def unpack_dict_to_list(source_dict: dict) -> list:
    dict_dishes = source_dict['Cook Book']

    list_with_lists_ingredients = []
    for dish in dict_dishes:
        list_with_lists_ingredients += dish.values()

    list_ingredients = []
    for i in list_with_lists_ingredients:
        list_ingredients.extend(i)
    return list_ingredients


def get_unique_ingredients(source_dict: dict) -> set:
    list_ingredients = unpack_dict_to_list(source_dict)
    unique_ingredients = set()

    for i in list_ingredients:
        unique_ingredients.add(i)

    return unique_ingredients


def get_count_ingredients(source_dict: dict) -> dict:
    list_ingredients = unpack_dict_to_list(source_dict)
    dict_count_and_name_ingredients = {}

    for j in list_ingredients:
        if j not in dict_count_and_name_ingredients:
            dict_count_and_name_ingredients[list_ingredients.count(j)] = j
    print(dict_count_and_name_ingredients)

    return dict_count_and_name_ingredients


def sort_count_ingredients(source_dict: dict) -> list:
    dict_count_and_name_ingredients = get_count_ingredients(source_dict)
    sort_dict_count_and_name_ingredients = dict(sorted(dict_count_and_name_ingredients.items(), reverse=True))
    return list(sort_dict_count_and_name_ingredients.values())


list_unique_ingredients = get_unique_ingredients(source_dict)
sort_ing = sort_count_ingredients(source_dict)
print(sort_ing)
