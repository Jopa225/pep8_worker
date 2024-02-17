# Create PEP8 reworker!
# PEP8 reworker should take one folder and go through all the subfolders looking for all *.py files
# Open every file and apply following PEP8 rules:
# Imports
# TAB and spaces
# Whitespaces
# Maximum length of line
# Spaces between functions
# In modules
# In classes

import argparse
import os

path = "pep8_folders"

parser = argparse.ArgumentParser(description="Trace event analyzer.")
parser.add_argument("--folder_path", type=str, help="Set the folder path to parse")

args = parser.parse_args()

# print(args.folder_path)


def get_py_files_paths_list(folder_path):
    py_files = []
    for roots, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith((".py")):
                py_files.append(os.path.join(roots, file))
    return py_files


def read_files_data(files_path):
    data = []
    for files in files_path:
        with open(files, "r", encoding="utf8") as file:
            data.append(file.readlines())
    return data


def write_data_to_files(files_path, data):
    i = 0
    for files in files_path:
        while i < len(files_path):
            with open(files, "w", encoding="utf8") as file:
                file.writelines(data[i])
            break
        i +=1


def pep8_append_EOF(data):
    for lst in data:
        if lst[-1][-1] != "\n":
            lst.append("\n")


def pep8_imports(data):
    for lst in data:
        j = 0
        idx_import = []
        for row in lst:
            if "from" in row and "," in row and "#" not in row:
                string_to_add = " "
                pep8_idx = row.index("from")
                from_word = row[row.index(" "):row.index("import")]
                lst[j] = row.replace(", ", string_to_add * pep8_idx + "\nfrom" + from_word + "import")
            elif "import" in row and "," in row:
                string_to_add = " "
                pep8_idx = row.index("import")
                lst[j] = row.replace(", ", string_to_add * pep8_idx + "\nimport")

            if row.startswith("import") or row.startswith("from"):
                idx_import.append(lst[j])

            j += 1
        for x in idx_import:
            del(lst[lst.index(x)])
        for x in reversed(idx_import):
            lst.insert(0, x)


###################                   replace for row in lst: with     for j, row in enumerate(lst):      remove j += 1 i j = 0
def pep8_line_ending79(data):
    for lst in data:
        j = 0
        for row in lst:
            if len(row) > 79: 
                idx = row.rindex(" ", 1, 79)
                new_line = " \\\n"
                if "=" in row and "def" not in row:
                    pep8_idx = row.index("=") + 2
                    string_to_add = " "
                if "def " in row and "(" in row:
                    pep8_idx = row.index("(")
                    string_to_add = " "
                    new_line = "\n"
                if "#" in row[0:20]:
                    pep8_idx = 1
                    string_to_add = "#"
                    new_line = "\n"
                
                row = row[:idx] + new_line + string_to_add * pep8_idx + row[idx:]
                row = row.split("\n")[:-1]
                
                while len(row[-1]) > 79:
                    idx = row[-1].rindex(" ", 1, 79)
                    row[-1] = row[-1][:idx] + new_line + string_to_add * pep8_idx + row[-1][idx:]
                    row.append(" ")
                    row[-2], row[-1] = row[-2].split("\n")[-2], row[-2].split("\n")[-1]
                    if len(row[-1]) < 79:
                        break
                    
                lst[j] = "\n".join(row)
                string_to_add = " "
            j += 1


def pep8_trailing_whitespaces(data):
    for lst in data:
        j = 0
        for row in lst:
            for i, element in enumerate(row):
                pass
                # if element == " " and row[i+1] == " ":
                #     row[i] = row[i].translate({32: None})#######################rip
            # if row.startswith(" ") not in row:
            # # for element in row:
            #     pass


def pep8_whitespaces(data):
    for lst in data:
        j = 0
        for row in lst:
            if "=" in row and "def" not in row:
                lst[j] = row.replace("=", " = ")
            if "," in row and ",)" not in row:
                lst[j] = row.replace(",", ", ")
            if "\t" in row:
                lst[j] = row.replace("\t", "    ")
            
            j += 1


def pep8_before_func_newline(data):
    for lst in data:
        del_data = []
        j = 0
        for row in lst:

            if row.startswith("\n") or row.startswith("    \n"):
                del_data.append(j)  
            if "def " in row and "self" not in row:
                lst[j] = "\n" + row
            idx_1 = j - 1 
            idx_2 = j - 2
            
            if "def " in row and (lst[idx_2] == "\n" and lst[idx_1] != "\n"):
                lst[j] = "\n\n" + row
            j += 1
        for x in reversed(del_data):
            if (x-1) in del_data:
                del(lst[x])
        # if "\n" in lst[0]:
        #     del(lst[0]) 
        if lst[-1].startswith("\n"):
            del(lst[-1]) 
        

def main(path):
    py_files = get_py_files_paths_list(path)
    data = read_files_data(py_files)
    
    pep8_whitespaces(data)
    
    pep8_before_func_newline(data)

    pep8_imports(data)

    
    
    pep8_line_ending79(data)

    pep8_append_EOF(data)

    pep8_trailing_whitespaces(data)
    # print(len(data))
    print(data[0])
    print(data[-1])
    print(len(py_files))
    print(len(data))




    # write_data_to_files(py_files, data)


main(path)
# main(args.folder_path)


