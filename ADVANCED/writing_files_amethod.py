#Python writing files (.txt, .json, .csv)

txt_data = "I like pizza !"
file_path = "ADVANCED/output.txt"

employess = ["Eugene", "Squidward", "Spongebob", "Patrick"]

# "w" write in the file; "r" read the file; "x" check if the file exists; "a" append the file

try:
    with open(file= file_path, mode= "a") as file:
        for employee in employess:
            file.write("\n" + employee) # "\n" new line
            print(f"{employee} was appended in the {file_path} file")
except FileNotFoundError:
    print(f"File {file_path} was not found")
