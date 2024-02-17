
lst = list()

for x in range(50, 201):
    lst.append(x)
# print(lst)

lst.remove(100)
# print(lst)

del lst[99]
# print(lst)

del lst[-6:]
# print(lst)

for x in lst:
    if(x % 3) == 0:
        lst.remove(x)

# print(lst)
res = sum(lst) / len(lst)


lst = lst[lst.index(124):]

print(res)
print(lst)

print(len(lst),sum(lst),min(lst),max(lst))


