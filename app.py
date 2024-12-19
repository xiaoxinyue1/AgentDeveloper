def solve_quadratic(a, b, c):
    # 计算判别式
    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:
        # 两个不同的实数解
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return (x1, x2)
    elif discriminant == 0:
        # 一个实数解
        x = -b / (2 * a)
        return (x,)
    else:
        # 无实数解
        return "No real solutions"


