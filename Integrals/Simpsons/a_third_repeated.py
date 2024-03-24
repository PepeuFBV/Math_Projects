def a_third_repeated(f, x0, xn, n):
    if n % 2 != 0:
        return "The number of subintervals must be even"
    h = (xn - x0) / n
    s = 0

    for i in range(1, n):
        x = x0 + i * h
        if i % 2 == 0:
            s += 2 * f(x)
        else:
            s += 4 * f(x)

    s += f(x0) + f(xn)
    return s * h / 3