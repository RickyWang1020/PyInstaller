"""
Function: reading config file, creating new folders, new python files and write contents into the python file
Author: Xinran Wang
Date: 08/04/2020
"""

import os
import yaml
import copy

def read_config(file_path):
    """
    Read the config file as a python dictionary
    :param file_path: the absolute path of the config file
    :return: a python dictionary
    """
    with open(file_path, "r") as y_file:
        config_file = yaml.load(y_file, Loader=yaml.FullLoader)
        return config_file

def read_from_template(temp_path):
    """
    Read the contents of the template python file (with two variables empty for further filling)
    :param temp_path: the absolute path of the template py file
    :return: a list containing the contents
    """
    with open(temp_path, "r") as temp:
        contents = temp.readlines()
        temp.close()
    return contents

def create_folder(directory, name):
    """
    Create a folder in the assigned directory with assigned name
    :param directory: the directory where the new folder will be located
    :param name: the folder's name
    :return: the absolute path of the folder (None if the folder already exists under the directory)
    """
    path = os.path.join(directory, name)
    exist = os.path.exists(path)
    if exist:
        print("The folder: " + path + " already exists, cannot create new folder")
        return
    else:
        os.mkdir(path)
        print("Created a new folder in: " + directory)
        return path

def create_py(target_dir, name):
    """
    Create a python file in the assigned directory with assigned name
    :param target_dir: the directory where the new py file will be located
    :param name: the name of the py file
    :return: the absolute path of the py file
    """
    file_path = os.path.join(target_dir, name + '.py')
    file = open(file_path, 'a+')
    print("Created " + name + '.py' + " in " + target_dir)
    file.close()
    return file_path

def edit_content(file_dir, to_write, test_id, description):
    """
    Make changes on the template's contents and add the test id and description to the new py file
    :param file_dir: the absolute path of the py file
    :param to_write: a python list containing the contents of the template
    :param test_id: the test id to fill in the file
    :param description: the description to fill in the file
    :return: None
    """
    to_write_copy = copy.deepcopy(to_write)
    to_write_copy[4] = to_write_copy[4].rstrip() + " '" + test_id + "'" + '\n'
    to_write_copy[5] = to_write_copy[5].rstrip() + " '" + description + "'" + '\n'
    with open(file_dir, "w") as f:
        f.writelines(to_write_copy)
        f.close()
