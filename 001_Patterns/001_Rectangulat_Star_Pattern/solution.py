def rectangular_star_pattern(n):
    if n == 0:
        return None 
    
    if n == 1:
        print("*")
        return None
    
    for i in range(n):
        print("*" * n)

rectangular_star_pattern(0)