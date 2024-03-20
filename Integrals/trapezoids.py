def trapezoidal_method(f, a, b, n):
    deltax = (b - a) / n
    area = 0
    fx1 = f(a)
    for i in range(n):
        xi = a + i * deltax
        if (i == (n-1)):
            fx2 = f(b)
        area += (2 * f(xi)) * deltax / 2
    extra = (fx1 + fx2) * deltax / 2
    return area + extra