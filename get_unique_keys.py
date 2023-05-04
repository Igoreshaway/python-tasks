source_dict = {"Cook Book": [
    {"Dish A": ["oil", "bacon", "oil"]},
    {"Dish B": ["eggs", "oil", "eggs"]}
]}

dict_ingredients = source_dict['Cook Book']


def dictionary_unpacking_to_a_list(dict_books: list[dict]) -> list:
    list_with_lists_ingredients = []
    for li in dict_books:
        list_with_lists_ingredients += li.values()

    list_with_ingredients = [x for l in list_with_lists_ingredients for x in l]
    return list_with_ingredients


def unique_ingredients(dict_books: list[dict]) -> list:
    list_ingredients = dictionary_unpacking_to_a_list(dict_books)
    list_unique_ingredients = []

    for i in list_ingredients:
        if i not in list_unique_ingredients:
            list_unique_ingredients.append(i)

    return list_unique_ingredients


def counting_the_ingredients(dict_books: list[dict]) -> list[int] and list[str]:
    list_ingredients = dictionary_unpacking_to_a_list(dict_books)
    list_unique_ingredients = unique_ingredients(dict_books)
    count_ingredient = []
    for i in list_unique_ingredients:
        count_ingredient.append(list_ingredients.count(i))

    return count_ingredient, list_unique_ingredients, list_ingredients


def sort_count_ingredients(dict_books: list[dict]) -> list:
    count_ingredients, list_unique_ingredients, list_ingredients = counting_the_ingredients(dict_books)
    sort_list_count_ingredients = sorted(count_ingredients, reverse=True)
    sort_list_ingredients = []
    for i in sort_list_count_ingredients:
        for j in list_ingredients:
            if i == list_ingredients.count(j) and j not in sort_list_ingredients:
                sort_list_ingredients.append(j)

    return sort_list_ingredients


list_unique_ingredients = unique_ingredients(dict_ingredients)
sort_ing = sort_count_ingredients(dict_ingredients)
print(sort_ing)
