# Function to find GCD (Greatest Common Divisor)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to find LCM (Least Common Multiple)
def lcm(a, b):
    return (a * b) // gcd(a, b)

# Function to find LCM of multiple numbers
def lcm_of_numbers(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result = lcm(result, num)
    return result

# Reading input
n = int(input("Enter the number of positive numbers: "))
numbers = list(map(int, input("Enter the positive numbers separated by space: ").split()))

# Calculating and printing the LCM
print("LCM:", lcm_of_numbers(numbers))
