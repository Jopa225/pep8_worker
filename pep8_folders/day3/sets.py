

sett1 = {68, 38, 4, 6, 58, 62, 93, 71, 56, 82, 52, 45, 35, 62, 56, 59, 71, 19, 45, 63}
sett2 = {95, 25, 9, 31, 4, 2, 17, 87, 62, 2, 58, 13, 71, 98, 38, 59, 42, 19, 66, 76, 31, 95}

unique = sett1 | sett2
print(unique)

unique = list(unique)
avg = 0
for i in range(0, len(unique)):
    avg = avg + unique[i]
avg = avg / len(unique)
print(avg)

res = list()
shared_val = sett1 & sett2
print(shared_val)
sett1 = sett1 - sett2
# sett1 = list(sett1)
# sett2 = list(sett2)
for i in sett1:
    if i not in sett2:
        res.append(i)###########

print(res)
print(sum(res))