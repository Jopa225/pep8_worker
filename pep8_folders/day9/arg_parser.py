# Create program arg_parser.py which takes up to 3 arguments (not including 0th argument).
# First argument tells how many lines are to be processed.
# Second argument tells which core is analyzed.
# Third argument tells which type is analyzed.
# Program will take csv file as an input (file used for parser exercises).
# If program is run with 3 arguments
# Requested number of lines are processed (first 2 lines skipped).
# Print all lines containing requested “core” and “type”.
# If program is run with 2 arguments, all lines are analyzed (2 skipped).
# Print all lines containing requested “core” and “type”.
# If program is run with 1 argument, all lines are analyzed for all cores.
# Print all lines containing requested “type”.
# If program is run with 0 arguments, program prints number of cores, and all detected types.
import sys
import parsing

# print(parsing.parsing("parser_input.csv")[1])
# print(sys.argv[1])

parsed_lst = parsing.parsing("parser_input.csv")

if len(sys.argv) == 1:
    lst_type = []
    lst_core = []
    for line in parsed_lst:
        if (line["type"]) not in lst_type:
            lst_type.append((line["type"]))
        if (line["core"]) not in lst_core:
            lst_core.append((line["core"]))
    print(lst_core)
    print(len(lst_core))
    print(lst_type)
        

if len(sys.argv) == 2:
    req_type = int(sys.argv[1])
    for line in parsed_lst:
        if int(line["type"]) == req_type:
            print(line)
    

if len(sys.argv) == 3:
    req_core = int(sys.argv[1])
    req_type = int(sys.argv[2])
    for line in parsed_lst:
        if int(line["core"]) == req_core and int(line["type"]) == req_type:
            print(line)
    

if len(sys.argv) == 4:
    # print(sys.argv)
    req_lines = int(sys.argv[1])
    req_core = int(sys.argv[2])
    req_type = int(sys.argv[3])
    parsed_lst = parsed_lst[:req_lines]
    # print(parsed_lst)
    for line in parsed_lst:
        if int(line["core"]) == req_core and int(line["type"]) == req_type:
            print(line)








