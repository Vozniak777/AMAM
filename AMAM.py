x = str(input("Введіть слово:"))
y = ""
for i in x[::-1]:
    y = y + i
print(y)