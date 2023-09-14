# 3. Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях. 
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. 
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга. 
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей. 
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

# 4. Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки 
# ферзей в задаче выше. Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

import random

# Проверяем, есть ли в данной расстановке ферзей пара, бьющая друг друга
def is_queens_safe(queens):
    for i in range(8):
        for j in range(i+1, 8):
            if queens[i][0] == queens[j][0] or queens[i][1] == queens[j][1] or abs(queens[i][0] - queens[j][0]) == abs(queens[i][1] - queens[j][1]):
                return False
    return True

# Генерируем случайную расстановку ферзей
def generate_random_queens():
    queens = []
    for _ in range(8):
        queens.append((random.randint(1, 8), random.randint(1, 8)))
    return queens

successful_arrangements = []
while len(successful_arrangements) < 4:
    queens_arrangement = generate_random_queens()
    if is_queens_safe(queens_arrangement):
        successful_arrangements.append(queens_arrangement)

for i, queens in enumerate(successful_arrangements):
    print(f"Successful arrangement #{i+1}:")
    for queen in queens:
        print(queen)
    print()
