import os


selected_dir = 'D:\\Study\\Python\\NetworkExplorer'


class Directory(object):
    def __init__(self, path):
        self.path = path
        self.dir_list = {}
        self.file_list = []

    def append_file(self, path):
        self.file_list.append(path)

    def append_directory(self, path, dir):
        self.dir_list[path] = dir


def find_dir(path):
    result = Directory(path)
    if os.path.isdir(path):
        for inner_path in os.listdir(path):
            sub_path = path + '\\' + inner_path

            if os.path.isdir(sub_path):
                result.append_directory(inner_path, find_dir(sub_path))
            else:
                result.append_file(inner_path)
    return result

dir_list = find_dir(selected_dir)
print(dir_list)