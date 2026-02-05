def right_angles_triangle_pattern(n):
    if n == 0:
        return None

    for i in range(1, n + 1):
        print("*" * i)


right_angles_triangle_pattern(4)
