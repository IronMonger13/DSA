def right_angled_number_pyramid(n):
    if n == 0:
        return None

    for rows in range(1, n + 1):
        for cols in range(1, rows + 1):
            print(cols, end="")
        print()


right_angled_number_pyramid(2)
