def lower(rows):
    print("\nLower Triangular Pattern\n")
    for i in range(1, rows + 1):
        print("*" * i)

def upper(rows):
    print("\nUpper Triangular Pattern\n")
    for i in range(rows, 0, -1):
        print("*" * i)

def pyramid(rows):
    print("\nPyramid Pattern\n")
    for i in range(1, rows + 1):
        spaces = " " * (rows - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)

rows = 10

lower(rows)
upper(rows)
pyramid(rows)
