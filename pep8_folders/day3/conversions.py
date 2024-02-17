
text = "deadbeef"

text = list(text)
print(text)
dec = list()
for i in text:
    dec.append(int(i, 16))

print(dec)  

res = sum(dec)

print(res)
print(bin(res))

res = bin(res)
print(res)
res = res[2::2]
print(res)
res = int(res,2)
print(res)
print(oct(res))######

