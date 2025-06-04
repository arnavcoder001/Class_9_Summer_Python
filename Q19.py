#This code displays the index number of elements entered.
user_input = input("Enter elements of the list separated by space: ")

my_list = user_input.split()

for i in range(len(my_list)):
    print(f"Index {i}: {my_list[i]}")