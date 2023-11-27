def parse_expression(expression):
    """
    Parse the expression into numbers and operators.
    """
    numbers = []
    operations = []
    number = ''
    
    for char in expression:
        if char in '+-*/':
            numbers.append(float(number))
            operations.append(char)
            number = ''
        else:
            number += char
    numbers.append(float(number))
    
    return numbers, operations

def calculate(a, b, op):
    """
    Perform a calculation based on the operator.
    """
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/': return a / b

def max_value_expression(expression):
    """
    Determine the arrangement of parentheses that maximizes the expression value.
    """
    numbers, operations = parse_expression(expression)

    # Initialize DP tables
    n = len(numbers)
    max_dp = [[0 for _ in range(n)] for _ in range(n)]
    min_dp = [[0 for _ in range(n)] for _ in range(n)]

    # Base case
    for i in range(n):
        max_dp[i][i] = min_dp[i][i] = numbers[i]

    # Fill DP tables
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            max_dp[i][j] = float('-inf')
            min_dp[i][j] = float('inf')

            for k in range(i, j):
                max_val = calculate(max_dp[i][k], max_dp[k + 1][j], operations[k])
                min_val = calculate(min_dp[i][k], min_dp[k + 1][j], operations[k])

                max_dp[i][j] = max(max_dp[i][j], max_val, calculate(min_dp[i][k], max_dp[k + 1][j], operations[k]))
                min_dp[i][j] = min(min_dp[i][j], min_val, calculate(max_dp[i][k], min_dp[k + 1][j], operations[k]))

    return max_dp[0][n - 1]




expression = "1-5+3*2-6+3"
max_value = max_value_expression(expression)
print(f"Max value for the expression '{expression}': {max_value}")
