
text = "This is my 1st 'Hello world!' example"

char10 = text[9]
print(char10)

text = "This is my 1st %s 'Hello world!' example"%("attempt to conquer")

print(text)

text = text.replace(" ", "!")
print(text)

text = text.split("!")
print(text)

text = text[:-2]
print(text)
new_text = list()
for i in text:
    if len(i) != 6:
        new_text.append(i)

print(new_text)


main = " ".join(new_text)
print(main)

new_text = main.upper()
print(new_text)

new_text = main.title()
print(new_text)

new_text = main.capitalize()
print(new_text)

