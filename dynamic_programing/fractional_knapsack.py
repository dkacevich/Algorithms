def fractional_knapsack(max_weight, weights, values):
    # Створення списку, що містить пари (цінність, вага, індекс)
    items = [(values[i], weights[i], i) for i in range(len(values))]
    # Сортування предметів за спаданням цінності на одиницю ваги
    items.sort(key=lambda x: x[0]/x[1], reverse=True)

    total_value = 0
    items_selected = []

    for value, weight, index in items:
        if max_weight - weight >= 0:
            # Якщо можемо взяти цілий предмет, беремо його
            max_weight -= weight
            total_value += value
            items_selected.append((values[index], 1))  # (індекс предмета, частка предмета)
        else:
            # Якщо не можемо взяти цілий предмет, беремо частину
            fraction = max_weight / weight
            total_value += value * fraction
            items_selected.append((values[index], fraction))
            break

    return total_value, items_selected

values = [60, 100, 120]  # Цінності предметів
weights = [10, 20, 30]   # Ваги предметів
max_weight = 50          # Максимальна вага рюкзака

max_value, items = fractional_knapsack(max_weight, weights, values)

print("Максимальна цінність:", max_value)
print("Предмети у рюкзаку:", items)

