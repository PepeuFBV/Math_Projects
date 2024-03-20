def rectangle_method(f, a, b, n):
    deltax = (b - a) / n
    area = 0
    for i in range(n):
        xi = a + i * deltax
        area += f(xi) * deltax
    return area
    