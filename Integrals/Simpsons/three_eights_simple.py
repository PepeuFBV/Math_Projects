def three_eights_simple(f, x0, x3, n):
    s = f(x0) + f(x3)
    h = (x3 - x0) / n
    x1 = x0 + h
    x2 = x1 + h
    s += 3 * (f(x1) + f(x2))
    return s * 3/8 * h