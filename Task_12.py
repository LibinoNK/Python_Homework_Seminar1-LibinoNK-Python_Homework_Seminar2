# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате
# по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

X = int(input("Введите X: "))
while X >= 1000 or X < 0:
    X = int(input("Введите X: "))

Y = int(input("Введите Y: "))
while Y >= 1000 or Y < 0:
    Y = int(input("Введите Y: "))

S = X+Y
P = X*Y

for first_num in range(1, 1001):
    for second_num in range(1, 1001):
        if first_num + second_num == S and first_num * second_num == P:
            print(first_num, second_num)
