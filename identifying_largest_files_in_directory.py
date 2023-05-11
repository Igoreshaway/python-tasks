import os

PATH_TO_DIRECTORY = './files_directory'


def get_files_path() -> list[str]:
    list_with_files_names_in_directory = os.listdir(PATH_TO_DIRECTORY)
    list_file_path = []
    for index in range(len(list_with_files_names_in_directory)):
        path_to_file = os.path.join(PATH_TO_DIRECTORY, list_with_files_names_in_directory[index])
        list_file_path.append(path_to_file)
    return list_file_path


def get_largest_files(number_files: int = 2) -> list[str]:
    file_paths = get_files_path()
    name_and_size_files = {}
    for file_path in file_paths:
        name_and_size_files[file_path.split('/')[-1]] = os.stat(file_path).st_size
    sorted_dict_with_path_and_size_file = dict(sorted(name_and_size_files.items(),
                                                      key=lambda x: x[1], reverse=True))
    sorted_files_names_by_size = list(sorted_dict_with_path_and_size_file.keys())
    return sorted_files_names_by_size[:number_files]


name_files = get_largest_files(3)
print(name_files)
