import csv
import os

employess = [["Name", "Age", "Job"],
    ["Eugene", 58, "Boss"], 
    ["Spongebob", 30, "Cook"],
    ["Patrick", 37, "Unemployed"],
    ["Sandy", 27, "Scientist"]
    ]


file_path = os.getcwd() + '/ADVANCED/outputs/output.csv'

try:
    with open(file= file_path, mode= "w", newline= '') as file: # the newline method will prevent output to have many empty lines
        writer = csv.writer(file)
        for row in employess:
            writer.writerow(row)

        print(f"csv file '{file_path}' was created")
except FileExistsError:
    print(f"file {file_path} already exists")