
file = open("demo_file.txt", "r")

num = file.read()
print(num)

new = num[::-1]
print(new)

res = int(num) * int(new)
print(res)

file = open("demo_file.txt", "w")
file.write(str(res))