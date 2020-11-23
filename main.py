#!/us/bin/env python3
# -*- coding: utf-8 -*-
import os


def get_files_list(dir_name):
    files = []
    for file in os.listdir(os.path.abspath(dir_name)):
        files.append(os.path.abspath(dir_name + '/' + file))
    return files


def read_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()


def sort_files(files_list):
    d = {}
    s = []
    for f in files_list:
        d.update({len(read_from_file(f)): f})
    list_keys = sorted(d.keys())
    for i in list_keys:
        s.append(d[i])
    return s


def merge_files(files_list):
    for file_path in files_list:
        content = read_from_file(file_path)
        with open('all_text.txt', 'a') as file:
            file.writelines(file_path + '\n')
            file.writelines(str(len(content)) + '\n')
            for c in content:
                file.write(c)
    return


if __name__ == '__main__':
    files_list = get_files_list('sorted')
    l = sort_files(files_list)
    merge_files(l)
