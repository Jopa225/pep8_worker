# Create file_handler module.
# In the module, define read_from_file() function which accepts filename as argument, reads it, converts it 
# to list (every line is one element of list) and returns the list.
# In the module, define write_to_file() function which for arguments accepts  filename and a list, function needs 
# to write to file where every list element represents new line.
# Create main program and import file_handler module.
# Create a file “builtins.txt” and fill it with Python builtins.
# From main program, read builtins.txt and count the lines

def read_from_file(file_name):
    file = open(file_name, "r")
    lista = []
    for line in file:
        lista.append(line[:-1])
    return lista

def write_to_file(file_name, lista):
    file = open(file_name, "w")
    for element in lista:
        file.write('%s\n' %element)

