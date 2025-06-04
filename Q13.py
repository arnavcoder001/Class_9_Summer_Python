#This code checks whether the number is Armstrong or not.
num = int(input("Enter a 3-digit number: "))

a = num // 100
b = (num // 10) % 10
c = num % 10

sum_of_cubes = a**3 + b**3 + c**3

if sum_of_cubes == num:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")