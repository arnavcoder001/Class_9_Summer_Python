#This code finds the factorial number.
num = int(input("Enter a number to find its factorial number: "))

factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(f"The factorial of {num} is {factorial}")