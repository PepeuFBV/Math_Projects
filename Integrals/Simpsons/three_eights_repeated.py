def three_eights_repeated(f, x0, xn, n):
    if n % 3 != 0:
        return "The number of subintervals must be a multiple of 3"
    
    h = (xn - x0) / n
    s = 0
    
    for i in range(1, n):
        x = x0 + i * h
        if i % 3 == 0:
            s += 2 * f(x)
        else:
            s += 3 * f(x)
            
    s += f(x0) + f(xn)
    return s * 3 * h / 8