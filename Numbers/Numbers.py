number = int(input("Введите число "))
if (number < 0) and (number % 2 == 0):
    print("Отрицательное четное число")
elif (number < 0) and (number % 2 == 1):
    print("Отрицательное нечетное число")
elif (number > 0) and (number % 2 == 0):
    print("Положительное четное число")
elif (number > 0) and (number % 2 == 1):
    print("Положительное нечетное число")
elif number == 0:
    print("Нулевое число")