"""
Function: read and pre-process .xml files
Author: Xinran Wang
Date: 08/04/2020
"""

from bs4 import BeautifulSoup as bs

def open_xml(path):
    """
    Open and preprocess the original .xml file
    :param path: the absolute path of the .xml file
    :return: a BeautifulSoup object that stores the whole text of .xml file
    """
    with open(path, "r", encoding='UTF-8', errors='ignore') as file:
        content = file.readlines()
        content = "".join(content)
        content = content.replace("<BR>", "")
        content = content.replace("</BR>", "")
        bs_content = bs(content, "lxml")
    return bs_content

def parse_test_cases(bs_file):
    """
    Parse the .xml texts by test cases
    :param bs_file: the BeautifulSoup object containing the whole text of .xml file (the output of open_xml)
    :return: a list containing every test case's .xml text as separate elements
    """
    result = []
    for x in bs_file.find_all("testcase"):
        result.append(x.find("title").text)
    return result

def generate_dic_and_decide_type(testcase_list):
    """
    Create a dictionary that separately stores the test case id and descriptions, also get the test type id number
    :param testcase_list: a list containing test case id + description strings
    :return: a tuple containing a python dictionary and a string representing the test type
    """
    dic = {}
    type = ""
    for t in testcase_list:
        first_colon = t.find(":")
        if first_colon == -1:
            print("Error when processing: " + t)
            return
        key = t[:first_colon]
        val = t[first_colon + 2:]
        dic[key] = val
        if not type:
            tc = t.split("_")[0]
            type = tc[2:]
    return dic, type
