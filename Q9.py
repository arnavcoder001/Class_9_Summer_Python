#This code checks which number is the biggest.
num1 = float(input("Enter a number: "))
num2 = float(input("Enter a number: "))
num3 = float(input("Enter a number: "))

if num1 >= num2 and num1 >= num3:
    biggest = num1
elif num2 >= num1 and num2 >= num3:
    biggest = num2
else:
    biggest = num3

print(f"The biggest number is {biggest:.2f}")