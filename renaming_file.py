import os

BASE_DIR_PATH = './1'


def get_path_to_file(paths_to_dir=None, result_paths_to_files=None):
    if paths_to_dir is None:
        paths_to_dir = [BASE_DIR_PATH]

    if result_paths_to_files is None:
        result_paths_to_files = []

    dir_paths = []
    for path in paths_to_dir:
        next_elements_in_path = os.listdir(path)
        for file in next_elements_in_path:
            full_path = os.path.join(path, file)
            if os.path.isfile(full_path):
                result_paths_to_files.append(full_path)
            else:
                dir_paths.append(full_path)

    if dir_paths:
        return get_path_to_file(dir_paths, result_paths_to_files)
    else:
        return result_paths_to_files


def get_rename_file():
    paths_files = get_path_to_file()
    rename_files = []
    for path_file in paths_files:
        filename = os.path.splitext(path_file)[0]
        rename_file = os.rename(path_file, filename + ".js")
        rename_files.append(rename_file)
    return rename_files


files = get_rename_file()
