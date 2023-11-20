def knapsack(weights, values, capacity):
    length = len(values)

    dp = [[0] * (capacity + 1) for _ in range(length + 1)]

    for i in range(1, length + 1):
        for w in range(capacity + 1):

            previous_item = dp[i - 1][w]
            current_weight = weights[i - 1]

            # If item weight is fitted
            if current_weight <= w:

                dp[i][w] = max(
                    previous_item,
                    values[i - 1] + dp[i - 1][w - current_weight]
                )
            else:
                dp[i][w] = previous_item

    selected_items = []

    i, w = length, capacity
    while i > 0 and w > 0:
        current_item = dp[i][w]
        previous_item = dp[i - 1][w]

        if current_item != previous_item:
            selected_items.append(i - 1)
            w -= weights[i - 1]
        i -= 1

    return dp[length][capacity], selected_items[::-1]


weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 7

max_value, selected_items = knapsack(weights, values, capacity)
print("Максимальна вартість:", max_value)
print("Обрані предмети:", selected_items)
