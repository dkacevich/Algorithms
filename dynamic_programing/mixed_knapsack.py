def mixed_knapsack_with_detailed_items(max_weight, full_items, fractional_items):
    # Сортування фракційних предметів за спаданням вартості за одиницю ваги
    fractional_items_sorted = sorted(enumerate(fractional_items), key=lambda x: x[1][1] / x[1][0], reverse=True)

    total_value = 0
    items_taken = []
    # Обробка повних предметів
    for i, (value, weight) in enumerate(full_items):
        if weight <= max_weight:
            max_weight -= weight
            total_value += value
            items_taken.append(('Full', value, 1))  # Повний предмет узято повністю
        else:
            # Переходимо до фракційних предметів, якщо не можна взяти повний
            break

    # Обробка фракційних предметів
    for i, (value, weight) in fractional_items_sorted:
        if weight <= max_weight:
            max_weight -= weight
            total_value += value
            items_taken.append(('Fractional', value, 1))  # Фракційний предмет узято повністю
        else:
            # Узято частину фракційного предмета
            fraction = max_weight / weight
            total_value += value * fraction
            items_taken.append(('Fractional Part', value, fraction))  # Частина фракційного предмета
            break

    return total_value, items_taken

full_items = [(100, 20), (60, 10)]       # Повні предмети: (цінність, вага)
fractional_items = [(120, 30), (70, 15)] # Фракційні предмети: (цінність, вага)
max_weight = 62

value, items = mixed_knapsack_with_detailed_items(max_weight, full_items, fractional_items)

print("Максимальна цінність:", value)
print("Предмети у рюкзаку:", items)


