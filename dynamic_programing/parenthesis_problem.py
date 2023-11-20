import operator


def calculate_max_expression(expression):
    # Функція для розбиття виразу на числа і оператори
    def split_expression(expr):
        numbers, operations = [], []
        current_number = ''
        for char in expr:
            if char in '+-*':
                numbers.append(int(current_number))
                current_number = ''
                operations.append(char)
            else:
                current_number += char
        numbers.append(int(current_number))
        return numbers, operations

    # Функція для визначення результату операції
    def apply_operation(op, a, b):
        if op == '+': return a + b
        elif op == '-': return a - b
        elif op == '*': return a * b

    # Розбиваємо вираз на числа і оператори
    numbers, operations = split_expression(expression)

    # Кількість чисел у виразі
    n = len(numbers)

    # Ініціалізація таблиць для зберігання мінімальних і максимальних значень
    min_val = [[0] * n for _ in range(n)]
    max_val = [[0] * n for _ in range(n)]

    # Заповнення діагоналі матриць, оскільки мінімум і максимум одного числа - це саме число
    for i in range(n):
        min_val[i][i] = max_val[i][i] = numbers[i]
        
    # Обрахунок мінімуму і максимуму для всіх підрядків
    for s in range(1, n):
        for i in range(n - s):
            j = i + s
            min_val[i][j] = float('inf')
            max_val[i][j] = float('-inf')
            for k in range(i, j):
                min_temp = apply_operation(operations[k], min_val[i][k], min_val[k + 1][j])
                max_temp = apply_operation(operations[k], max_val[i][k], max_val[k + 1][j])

                min_val[i][j] = min(min_val[i][j], min_temp, max_temp)
                max_val[i][j] = max(max_val[i][j], min_temp, max_temp)

   
   
    # Повернення найбільшого числа
    return max_val[0][n - 1]






expression = "10-5*2+2"
max_value = calculate_max_expression(expression)
print(max_value)
