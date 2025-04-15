#Python writing files (.txt, .json, .csv)

txt_data = "I like pizza !"
file_path = "ADVANCED/output.txt"



# "w" write in the file; "r" read the file; "x" check if the file exists; "a" append the file
# if has no file in directory, then "w - write" method will create it

with open(file = file_path, mode="w") as file: 
     file.write(txt_data)
     print(f"txt file '{file_path}' was created")


