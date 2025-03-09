#!/usr/bin/env python3

def print_fibonacci(n):
    fibonacci_list = [0, 1]  # Start with the first two numbers

    for _ in range(n - 2):
        next_number = fibonacci_list[-1] + fibonacci_list[-2]  # Sum of last two elements
        fibonacci_list.append(next_number)

    print(fibonacci_list[:n])  # Print only the first `n` elements
