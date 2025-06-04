# Input elements separated by space
user_input = input("Enter elements of the list separated by space: ")

my_list = user_input.split()

# Print each element with its index
for i in range(len(my_list)):
    print(f"Index {i}: {my_list[i]}")