# Lab1/Zadanie 1
print("Podaj nazwę pliku tekstowego: ")
file_name = input()
with open(file_name, 'r') as firstfile, open ('lab1zad1.txt', 'a') as secondfile:
    for line in firstfile:
        secondfile.write(line)

