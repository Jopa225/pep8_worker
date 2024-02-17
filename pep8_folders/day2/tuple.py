
tipla = ()

for x in range(50, 201):
    tipla += (x,)
tipla1 = ()
tipla2 = ()

print(tipla)
for x in tipla:
    tipla1 = tipla[:51] + tipla[100:]

print(tipla1)
index = ()
index += (tipla1.index(167),)

print(index)
index += (tipla1)
print(index)
print(sum(index))
