def swap_with_variable(a, b):
    c = a
    a = b
    b = c
    return a, b

# Example usage
num1 = 5
num2 = 7

print("Before swapping:", num1, num2)
num1, num2 = swap_with_variable(num1, num2)
print("After swapping:", num1, num2)


def swap_without_variable(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b

# Example usage
num1 = 10
num2 = 20

print("Before swapping:", num1, num2)
num1, num2 = swap_without_variable(num1, num2)
print("After swapping:", num1, num2)
