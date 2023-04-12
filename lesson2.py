# Задача 1. Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.
# пусть N = 4 -> [1, 2, 6, 24](1, 1*2, 1*2*3, 1*2*3*4)

def task1():
    n = int(input("Введите число: "))
    count = 1
    for i in range(1, n+1):
        count *= i
        print(count)

# Задача 2. Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.


def task2():
    print("x | y | z | ¬(X ∧ Y) ∨ Z")
    for x in range(2):
        for y in range(2):
            for z in range(2):
                print(f"{x} | {y} | {z} | {int(not(x and y) or z)}")
# Задача 3. Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2


def task3():
    str1 = input("Введите первую строку: ")
    str2 = input("Введите вторую строку: ")
    len_str1 = len(str1)
    len_str2 = len(str2)

    for i in range(len_str1):
        count = 0
        for x in range(len_str2):
            if str1[i] == str2[x]:
                count += 1
        print(
            f'Символ "{str1[i]}" из первой строки встречается в строке "{str2}" - {count} раз(-a)')


# Задача 4. Задайте список из N элементов, заполненных числами из промежутка[-N, N]. Сдвиньте все элементы списка на 2 позиции вправо.
# 3 -> [2, 3, -3, -2, -1, 0, 1]

def task4():
    num = int(input("Введите число: "))
    num_list = []

    for i in range(-num, num+1):
        num_list.append(i)

    num_list = num_list[-2:] + num_list[:-2]
    print(num_list)


task3()
