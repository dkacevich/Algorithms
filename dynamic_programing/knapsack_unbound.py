def unbounded_knapsack_with_items(max_weight, weights, values):
    n = len(values)
    dp = [0 for _ in range(max_weight + 1)]
    items_selected = [[] for _ in range(max_weight + 1)]

    for w in range(1, max_weight + 1):
        for i in range(n):
            if weights[i] <= w and dp[w] < dp[w - weights[i]] + values[i]:
                dp[w] = dp[w - weights[i]] + values[i]
                items_selected[w] = items_selected[w - weights[i]] + [i]

    return dp[max_weight], [weights[i] for i in items_selected[max_weight]]


values = [60, 100, 120]  # Цінності предметів
weights = [15, 17, 18]   # Ваги предметів
max_weight = 70        # Максимальна вага рюкзака

max_value, items = unbounded_knapsack_with_items(max_weight, weights, values)
print("Максимальна цінність:", max_value)
print("Предмети у рюкзаку:", items)
