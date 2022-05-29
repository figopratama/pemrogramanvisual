
for row in range(1, 11):
    if row < 10:
        print(row, " =", end="")
    if row == 10:
        print(row, "=", end="")

    for col in range(1, 11):
        num = row * col
        if num < 10:
            empty = "  "
        else:
            if num < 10:
                empty = " "
        if col == 1:
            if row == 1:
                print(" ", row, end='')
            else:
                print(" ", row, end='')
        elif row == 1:
            print("  ", col, end='')
        else:
            print(empty, num, end='')
    print()
    
    
    
