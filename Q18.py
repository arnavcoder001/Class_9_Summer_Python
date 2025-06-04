#This code displays the sum of odd numbers.
numbers = [3, 8, 5, 12, 7, 10, 15, 2]

odd_sum = 0
odd_numbers = []

for num in numbers:
    if num % 2 != 0:
        odd_numbers.append(num)
        odd_sum += num

print("Odd numbers in the list:", odd_numbers)
print("Sum of odd numbers:", odd_sum)