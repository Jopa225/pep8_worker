
binary = 0b10010
print(binary)

binary = binary<<12
print(binary)

binary = binary ^ 0b10010000001001000
print(binary)

binary = binary>>2
print(binary)

print(0b10010 == binary)