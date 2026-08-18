# Get the number of rows from the user
n = int(input("Enter number of rows: "))

# Top half
for i in range (1, n + 1):
    # Print spaces
    for j in range (n - i):
        print(" ", end="")

    # Print numbers
    for j in range (1, 2 * i):
        print (j, end="")

    print()

# Bottom half
for i in range (n - 1, 0, -1):
    # Print spaces
    for j in range(n - i):
        print(" ", end="")

    # Print numbers
    for j in range(1, 2 * i):
        print(j, end="")

    print()
