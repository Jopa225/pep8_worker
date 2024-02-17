
imut = [1,2,3,4,5]
print(id(imut))

imut.append(2)
print(imut)

print(id(imut))


mut = 1
print(id(mut))

mut = mut + 1
print(mut)
print(id(mut))
