# 0-1 Knapsack Problem using Dynamic Programming

def knapsack(weights, values, capacity):
    n = len(values)
    # Create DP table with dimensions (n+1) x (capacity+1)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build the DP table in bottom-up manner
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                # Either include the item or exclude it
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]],
                               dp[i - 1][w])
            else:
                # Cannot include the item
                dp[i][w] = dp[i - 1][w]

    # The bottom-right cell contains the maximum value
    return dp[n][capacity], dp


# --- Main program ---
n = int(input("Enter number of items: "))
weights = []
values = []

print("\nEnter weight and value for each item:")
for i in range(n):
    w = int(input(f"Weight of item {i+1}: "))
    v = int(input(f"Value of item {i+1}: "))
    weights.append(w)
    values.append(v)

capacity = int(input("\nEnter the capacity of knapsack: "))

max_value, dp_table = knapsack(weights, values, capacity)

print("\nMaximum value that can be obtained:", max_value)

print("\nDynamic Programming Table:")
for row in dp_table:
    print(row)
