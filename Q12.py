#This code displays the multiplication.
num = int(input("Enter a number to multiply: "))

print(f"Multiplication of table {num}")
for i in range(1,11):
    print(f"{num} x {i} = {num * i}")