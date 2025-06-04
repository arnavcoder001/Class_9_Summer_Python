#This code displays odd and even numbers
print("Odd numbers from 1 to 50:")
for i in range(1, 51):
    if i % 2 != 0:
        print(i, end=" ")

print("\nEven numbers from 1 to 50:")
for i in range(1, 51):
    if i % 2 == 0:
        print(i, end=" ")
