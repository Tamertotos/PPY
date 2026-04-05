text = input("Enter a sentence\n")
print(len(text))
text2 = text.replace(" ", "_")
print(text2)
print(id(text))
print(id(text2))
text3 = text.split()
print(text3)


print(text[0:3:1])
print(text[-1:-5:-1])
print(text[len(text)-4:len(text) : 1])

print("There are " , text.count(" ") + 1 ,  " sentences in the text")

countDigit = 0
for char in text:
    print(char)
    if char.isdigit():
        countDigit += 1

print(f"There are {countDigit} digits in the text")

if text.isdigit() == True:
    print("Text is digit")
elif text.isalpha() == True:
    print("Text is string")
else:
    print("Text consists of digit and string")

if text.lower().count("python") > 0:
    print("Text consists of python")
    print(text.lower().replace("python","JAVA"))

print("text contains a " , text.lower().count("a"), " times")

print("Hello World!".split())