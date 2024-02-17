
res = 0
counter = 0
for i in range(0,100):
    
    if((i % 5) == 0 and (i % 10) == 5):
        continue
    if i in range(50,60):
        continue
    print(i)
    counter += 1
    res += i

print(res/counter)
print(counter)
res = 0
counter = 0
index = 0
while(index < 100):
    
    
    if((index % 5) == 0 and (index % 10) == 5):
        index += 1
    if index in range(50,60):
        index += 10
    print(index)
    res += index
    index += 1
    counter += 1
    
print(res/counter)
print(counter)
res = 0
counter = 0
index = 0
while(True):
    
    if((index % 5) == 0 and (index % 10) == 5):
        index += 1
    if index in range(50,60):
        index += 10
    print(index)
    res += index
    index += 1
    counter += 1
    if(index == 100):
        break
    
    
print(res/counter)
print(counter)
