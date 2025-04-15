#python file detection

import os

file_path = "C:/Users/30887/Desktop/py/pyth/learning_python-main/ADVANCED/stuff"

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")
    
    if os.path.isfile(file_path): # checks if the file is a file
        print("That is a file")
    elif os.path.isdir(file_path): # checks if the file is a directory
        print("That is a directory")
    
else:
    print(f"The location doesn't exists")
    
    
    