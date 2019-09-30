

## Locally save and call this file ex.py ##

# Code to demonstrate the use of some of the OS modules in python

import os

# Let us print the files in the directory in which you are running this script
# print(os.listdir("."))
#
# # Let us check if this file is indeed a file!
# print(os.path.isfile("./ex.py"))
#
# # Does the file end with .py?
# print("./ex.py".endswith(".py"))


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    c_files = list()

    if (suffix is None or len(suffix) == 0) or (path is None or not os.path.isdir(path)):
        if (suffix is None or len(suffix) == 0) and (path is None or not os.path.isdir(path)):
            print("Invalid path : {0} and suffix : {1}".format(path, suffix))
        elif suffix is None or len(suffix) == 0:
            print("Invalid suffix : {0}".format(suffix))
        else:
            print("Invalid path : {0}".format(path))
    else:
        c_files = find_files_recursive(suffix, path, c_files)

    print("Total files found : {0}".format(len(c_files)))
    print(c_files)


def find_files_recursive(suffix, path, c_files):

    for item in os.listdir(path):
        abs_path = path + "/" + item
        if os.path.isfile(abs_path) and abs_path.endswith(suffix):
            c_files.append(abs_path)
        elif os.path.isdir(abs_path):
            find_files_recursive(suffix, abs_path, c_files)

    return c_files


find_files('.c', "./testdir1")

find_files('.c', "./testdir")
# ['./testdir/subdir1/a.c', './testdir/subdir3/b4.c', './testdir/subdir3/subsubdir1/b.c', './testdir/subdir5/a.c', './testdir/t1.c']

find_files('.k', "./testdir")
# returns and empty list
find_files('.h', "./testdir")
# ['./testdir/subdir1/a.h', './testdir/subdir3/subsubdir1/b.h', './testdir/subdir5/a.h', './testdir/t1.h']

find_files('.exe', "./testdir")
# returns and empty list

find_files('', "./testdir")
# returns and empty list

find_files(None, None)
# returns and empty list
