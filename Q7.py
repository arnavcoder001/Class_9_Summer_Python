#This code checks whether the number entered by the user is multiple of 11 or not.
num=int(input("Enter a number to check if multiple of 11 or not: "))

if num % 11 == 0:
    print("This number is a multiple of 11.")
else:
    print("This number is not a multiple of 11.")