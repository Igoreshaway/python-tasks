source_dict = {"Cook Book": [
    {"Dish A": ["oil", "bacon", "oil"]},
    {"Dish B": ["eggs", "oil", "eggs"]}
]}

dict_ingredients = source_dict['Cook Book']


def dictionary_unpacking(dict_books: list[dict]) -> list:
    list_with_list_ingred = []
    for li in dict_books:
        list_with_list_ingred += li.values()

    list_with_ingred = [x for l in list_with_list_ingred for x in l]
    return list_with_ingred


def unique_ingredients(dict_books: list[dict]) -> list:
    list_ing = dictionary_unpacking(dict_books)
    list_unique_ing = []

    for i in list_ing:
        if i not in list_unique_ing:
            list_unique_ing.append(i)

    return list_unique_ing


def counting_list(dict_books: list[dict]) -> list[int] and list[str]:
    list_ing = dictionary_unpacking(dict_books)
    list_uniq_ing = unique_ingredients(dict_books)
    count_ing = []
    for i in list_uniq_ing:
        count_ing.append(list_ing.count(i))

    return count_ing, list_uniq_ing, list_ing


def sort_count_ingredients(dict_books: list[dict]) -> list:
    count_ing, list_uniq_ing, list_ing = counting_list(dict_books)
    sort_count_ing = sorted(count_ing, reverse=True)
    sort_list_ing = []
    for i in sort_count_ing:
        for j in list_ing:
            if i == list_ing.count(j) and j not in sort_list_ing:
                sort_list_ing.append(j)

    return sort_list_ing


list_unique_ingredients = unique_ingredients(dict_ingredients)
sort_ing = sort_count_ingredients(dict_ingredients)
print(sort_ing)
