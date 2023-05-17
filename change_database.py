import re

PATH_TO_DATABASE = 'old_file'
PATH_TO_NEW_DATABASE = 'new_file'
result = {
    '1': 'Иван',
    '2': 'Олег',
    '4': 'Артём'
}

result_copy = result.copy()


def write_new_file(result: dict):
    with open(PATH_TO_DATABASE, 'r') as file:
        lines = file.readlines()

    result_copy = result.copy()
    with open(PATH_TO_NEW_DATABASE, 'r+') as new_file:
        for line in lines:
            number_in_old_file, name_in_old_file = line.split()
            for number_in_result, name_in_result in result.items():
                if number_in_old_file == number_in_result and name_in_old_file == name_in_result:
                    new_file.write(line)
                    del result_copy[number_in_result]
                elif number_in_old_file == number_in_result and name_in_old_file != name_in_result:
                    new_file.write(line.replace(name_in_old_file, name_in_result))
                    del result_copy[number_in_result]
                elif number_in_old_file not in result.keys():
                    pass
                elif number_in_result not in new_file:
                    new_file.write(f'{number_in_result} {name_in_result}' + '\n')
                    del result_copy[number_in_result]
                if not result_copy:
                    return new_file



ch_db = write_new_file(result)
print(ch_db)
