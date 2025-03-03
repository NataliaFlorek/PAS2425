#Lab1/Zadanie 2
# Lab1/Zadanie 1
print("Podaj nazwę obrazka: ")
file_name = input()
with open(file_name, 'rb') as firstfile, open ('lab1zad1.png', 'ab') as secondfile:
    for line in firstfile:
        secondfile.write(line)

