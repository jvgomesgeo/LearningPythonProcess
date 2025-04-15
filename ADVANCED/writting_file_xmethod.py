#Python writing files (.txt, .json, .csv)

txt_data = "I like pizza !"
file_path = "ADVANCED/output.txt"



#this will check if output file is in the directory, if not, it'll be created
try:
    with open(file = file_path, mode = "x") as file:
        file.write(txt_data)
        print(f"txt file '{file_path}' was created")
except FileExistsError:
    print("That file already existis")
