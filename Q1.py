#This code checks whether the number is prime or not.

n=int(input("Enter a number: "))

for i in range(2, n-1):
    if n % i == 0:
        print("Not a prime number.")
        exit()   
print("Prime number")
