# Get the number of rows from the user
n = int(input("Enter a number: "))

# Outer loop controls the number of rows
for i in range(1, n + 1):

    # Inner loop controls how many times the number is printed
    for j in range(i):
        print(i, end=" ")

    # Move to the next row
    print()