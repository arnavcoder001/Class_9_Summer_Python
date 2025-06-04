#This code display patterns.
n = 15
for i in range(1, n+1):
    if i < n:
        print(i, end=" + ")
    else:
        print(i)


n = 15
for i in range(1, n + 1):
    if i < n:
        if i % 2 == 0:
            print(f"{i} - ", end="")
        else:
            print(f"{i} + ", end="")
    else:
        print(i)