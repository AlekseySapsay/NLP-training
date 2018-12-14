#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os.path
import nltk


import all_functions as af



# fot test it you need and make exception :

# 1 time when the system is not installed along the default path,
# 1 time when the system is not installed along the path specified by the user,
# 1 again when the system is already installed and
# 1 time if the path is incorrect

# fix it! Why path from user not used like path to folder for download?
# In that part I can check dir exists. And select place to dir, and make dir if it is not exist.

path = os.path.abspath(raw_input("Enter path to download nltk,or press enter and path to folder will be default:\n"))

#print(type(path))
#print(path)
def setup(path = "C:\\nltk_data"):
    try:
        print("make dir nltk_data")
        print("****downloading nltk****")
        os.makedirs(path)
        nltk.download()
    except OSError:
        if not os.path.isfile(path):
            print("nltk already exist and will be not download")




def main():
    setup()
    text = "Adj are most interesting part o speech"
    res = af.parse_text(text)
    print(res)


if __name__=="__main__":
    main()




# if module file is exist -> break
# else:
#    input() or default path
# and I need add exeption if path is not exist

# the code should contain all necessary input data checks, for example, if the path to the folder is passed to the input,
# you need to check that it exists, if it does not exist, try to create, if it fails to throw an exception, where the
# message contains details, for example, "Failed to create directory '/ path / to / file' ". On the other hand,
# there is no need to duplicate checks: if the list is checked for non-emptyness in the first function,
# there is no point in doing another check in the functions that are called from it.



""" 
# in that part I cheking the path to nltk dir, if it exist
# if len of path == 0, then we need to download nltk and other requiremtns?

def find(name, path):
    for root, dirs, files in scandir.walk(path):
        if root.endswith(name):
            return root

def find_nltk_data():
    start = time.time()
    path_to_nltk_data = find('nltk_data', '/')
    print >> sys.stderr, 'Finding nltk_data took', time.time() - start
    print >> sys.stderr,  'nltk_data at', path_to_nltk_data
    with open('where_is_nltk_data.txt', 'w') as fout:
        fout.write(path_to_nltk_data)
    return path_to_nltk_data

def magically_find_nltk_data():
    if os.path.exists('where_is_nltk_data.txt'):
        with open('where_is_nltk_data.txt') as fin:
            path_to_nltk_data = fin.read().strip()
        if os.path.exists(path_to_nltk_data):
            nltk.data.path.append(path_to_nltk_data)
        else:
            nltk.data.path.append(find_nltk_data())
    else:
        path_to_nltk_data  = find_nltk_data()
        nltk.data.path.append(path_to_nltk_data)


magically_find_nltk_data()
print nltk.pos_tag('this is a foo bar'.split())

"""
