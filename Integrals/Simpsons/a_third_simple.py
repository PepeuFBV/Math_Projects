def a_third_simple(f, x0, x2):
    x1 = (x0 + x2) / 2
    h = (x2 - x0) / 2
    return (h/2) * (f(x0) + 4 * f(x1) + f(x2)) / 3