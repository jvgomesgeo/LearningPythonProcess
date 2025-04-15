#Python writing files (.json, .csv)

import json
file_path = "ADVANCED/output.json"

employee = {
    'name': 'Spongebob',
    'age': 30,
    'job': 'Cook'
}

# "w" write in the file; "r" read the file; "x" check if the file exists; "a" append the file
try:
    with open(file= file_path, mode= "w") as file: 
        json.dump(employee, file, indent=4 )#indent will format the output to be indented, more readable
        print(f"json file '{file_path}' was created ")
except FileNotFoundError:
    print(f"File '{file_path}' was not found")
