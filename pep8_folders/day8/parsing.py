# Create your own module which will be capable of parsing.
# Function for parsing will receive input file.
# Input file is available on this link.
# Input file is csv (comma separated values).
# If line starts with #, line is ignored.
# For each line, one dictionary should be created:
# Keys are strings from line 2
# Values are corresponding values in each line
# Return list of created dictionaries

file = open("parser_input.csv", "r")

lines = file.readlines()

res = []
dic = {}
keys = []
lst = list()

for line in lines:
    if line.startswith("#HEADER"):
        keys = line.split(",")
        keys[0] = keys[0][-3:]
        keys[-1] = keys[-1][:-1]
    if line.startswith("#"):
        continue
    
    dic = {}
    res = line.split(",")
    res[-1] = res[-1][:-1]
    for i in range(0, len(res)):
        dic[keys[i]] = res[i]
    lst.append(dic)
    # lst.append({str(keys) : res})
    # lst.append({keys[0]: res[0], keys[1]: res[1],"host": res[2],"core": res[3],"type": res[4],"swc": res[5],"rid": res[6],"data": res[7]})

print(lst)
print(keys)

print(len(lst))
print(lst[-1])
print(lst[2])
print(lst[0])



file.close()







