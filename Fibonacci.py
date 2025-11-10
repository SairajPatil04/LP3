import time
import sys

# --- Recursive Fibonacci Function ---
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# --- Non-Recursive (Iterative) Fibonacci Function ---
def fibonacci_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

# --- Recursive Series Printer ---
def print_fibonacci_recursive_series(n):
    for i in range(n):
        print(fibonacci_recursive(i), end=" ")

# --- Menu-Driven Program ---
while True:
    print("\n========== Fibonacci Series Menu ==========")
    print("1. Recursive Method")
    print("2. Non-Recursive (Iterative) Method")
    print("3. Exit")
    choice = int(input("Enter your choice (1-3): "))

    if choice == 1:
        n = int(input("Enter the number of terms: "))
        print("\nFibonacci Series (Recursive):")
        start_time = time.time()
        print_fibonacci_recursive_series(n)
        end_time = time.time()

        print("\n\n--- Time & Space Complexity Analysis ---")
        print(f"Execution Time: {end_time - start_time:.6f} seconds")
        print("Time Complexity : O(2^n)")
        print("Space Complexity: O(n)   (due to recursive call stack)")

    elif choice == 2:
        n = int(input("Enter the number of terms: "))
        print("\nFibonacci Series (Iterative):")
        start_time = time.time()
        fibonacci_iterative(n)
        end_time = time.time()

        print("\n\n--- Time & Space Complexity Analysis ---")
        print(f"Execution Time: {end_time - start_time:.6f} seconds")
        print("Time Complexity : O(n)")
        print("Space Complexity: O(1)   (uses constant memory)")

    elif choice == 3:
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice! Please select 1, 2, or 3.")
