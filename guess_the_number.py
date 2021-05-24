import numpy as np

'''Загадано число от 1 до 100, необходимо отгадать его за меньшее количество попыток'''
number = np.random.randint(1, 101)  # загаданное число
print("Загадано число от 1 до 100")


def binary_search(number):
    count = 0  # счетчик попыток
    lower_bound = 0
    upper_bound = 100
    while lower_bound <= upper_bound:
        middle = (lower_bound + upper_bound) // 2
        count += 1  # плюсуем попытку

        if number == middle:
            return middle

        elif number > middle:
            upper_bound = middle - 1
        elif number < middle:
            lower_bound = middle + 1
    print(f"Вы угадали число {number} за {count} попыток.")


binary_search(number)
