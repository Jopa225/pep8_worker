import argparse
import os
import re
import shutil


parser = argparse.ArgumentParser(description="Trace event analyzer.")
parser.add_argument("--folder_path", "-f", type=str,
                    help="Set the folder path to parse")
parser.add_argument("--apply_changes", "-a", action="store_true",
                    help="Apply changes that pep8parser made in _temp \
                        file to actual file")

args = parser.parse_args()


def copy_py_files(py_files):
    copied_files = list()
    for file in py_files:
        file_copy = file[:-3] + "_temp" + file[-3:]
        if "_temp" not in file:
            print(f"Copying file {file}")
            shutil.copyfile(file, file_copy)
            copied_files.append(file_copy)
    return copied_files


def apply_file_changes(py_files):
    for file in py_files:
        if "_temp" in file:
            continue
        file_copy = file[:-3] + "_temp" + file[-3:]
        print(f"Apply changes to original file {
              file}, then remove {file_copy}")
        shutil.copy(file_copy, file)
        if os.path.exists(file_copy):
            os.remove(file_copy)


def get_py_files_paths_list(folder_path):
    print(f"Finding all .py files in {folder_path}")
    py_files = []
    for roots, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith((".py")):
                py_files.append(os.path.join(roots, file))
    return py_files


def read_files_data(files_path):
    print(f"Reading data of all files and storing it in \"data\" variable")
    data = []
    for files in files_path:
        with open(files, "r", encoding="utf8") as file:
            data.append(file.readlines())
    return data


def write_data_to_files(files_path, data):
    print("Writing \"data\" to _temp files")
    for i, files in enumerate(files_path):
        while i < len(files_path):
            with open(files, "w", encoding="utf8") as file:
                file.writelines(data[i])
            break


def pep8_append_EOF(data):
    print("Append EOF")
    for lst in data:
        if "\n" not in lst[-1][-1]:
            lst.append("\n")


def pep8_imports(data):
    for lst in data:
        idx_import = []
        for j, row in enumerate(lst):
            if "from" in row and "," in row and "#" not in row:
                from_word = row[row.index(" "):row.index("import")]
                lst[j] = row.replace(", ", "\nfrom" + from_word + "import")
            elif "import" in row and "," in row:
                lst[j] = row.replace(", ",  "\nimport ")

            if "import" in row:
                idx_import.append(lst[j])

        # Delete all imports
        for x in idx_import:
            del (lst[lst.index(x)])
        # Set all imports at start of file
        for x in reversed(idx_import):
            lst.insert(0, x.lstrip())


def pep8_line_ending79(data):
    for lst in data:
        for j, row in enumerate(lst):
            if len(row) > 79:
                print(f"Detected line over 79 characters at index: {j + 1}")
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

                row = row[:idx] + new_line + \
                    string_to_add * pep8_idx + row[idx:]
                row = row.split("\n")[:-1]

                while len(row[-1]) > 79:
                    idx = row[-1].rindex(" ", 1, 79)
                    row[-1] = row[-1][:idx] + new_line + \
                        string_to_add * pep8_idx + row[-1][idx:]
                    row.append(" ")
                    row[-2], row[-1] = row[-2].split(
                        "\n")[-2], row[-2].split("\n")[-1]
                    if len(row[-1]) < 79:
                        break

                lst[j] = "\n".join(row) + "\n"
                string_to_add = " "


def pep8_whitespaces(data):
    for lst in data:
        for j, row in enumerate(lst):
            if "=" in row and "def" not in row and re.findall(r"=([+\-*\/%^&|<>])", row) and "==" not in row:
                row = row.replace("=", " = ")
            if "," in row and ",)" not in row:
                row = row.replace(",", ", ")
            if "\t" in row and "\"" not in row:
                row = row.replace("\t", "    ")

            # Remove all extra spaces not including indent
            if re.search('[a-zA-Z]', row):
                idx = re.search('[a-zA-Z]', row)
                if idx is not None:
                    idx = idx.start()
                saved_spaces = ""
                if not row.isspace() and not "\"\"\"" in row:
                    saved_spaces = row[:idx]
                row = re.sub(" +", " ", row[idx:])

                if " =" in row and "def" in row:
                    row = row.replace(" =", "=")
                if "= " in row and "def" in row:
                    row = row.replace("= ", "=")
                if " = " in row and "def" in row:
                    row = row.replace(" = ", "=")

                lst[j] = saved_spaces + row


def pep8_before_func_newline(data):
    for lst in data:
        del_data = []
        for j, row in enumerate(lst):
            if row.isspace():
                del_data.append(j)

            idx_1 = j - 1
            idx_2 = j - 2
            # Add the needed numbers of newlines before function definition
            if "def " in row and "self" in row and lst[idx_1].isspace():
                lst[j] = row
            elif "def " in row and "self" in row:
                lst[j] = "\n" + row
            else:
                if "def " in row and not lst[idx_2].isspace() and not lst[idx_1].isspace():
                    lst[j] = "\n\n" + row
                if "def " in row and (lst[idx_2].isspace() and not lst[idx_1].isspace()):
                    lst[j] = "\n\n" + row
                if "def " in row and (lst[idx_1].isspace() and not lst[idx_2].isspace()):
                    lst[j] = "\n" + row
                if "def " in row and (lst[idx_1].isspace() and lst[idx_2].isspace()):
                    lst[j] = "\n" + row

        # Remove extra newlines between all lines in file
        for x in reversed(del_data):
            if (x-1) in del_data:
                print(f"Remove extra newline at index {x}")
                del (lst[x])
        if lst[-1].isspace():
            del (lst[-1])


def main(path):

    py_files = get_py_files_paths_list(path)

    if args.apply_changes:
        apply_file_changes(py_files)
    else:
        copied_py_files_paths = copy_py_files(py_files)

        data = read_files_data(copied_py_files_paths)

        pep8_whitespaces(data)
        pep8_line_ending79(data)

        pep8_imports(data)

        pep8_before_func_newline(data)
        pep8_append_EOF(data)

        write_data_to_files(copied_py_files_paths, data)


# path = "pep8_folders\day6"
# main(path)
main(args.folder_path)
