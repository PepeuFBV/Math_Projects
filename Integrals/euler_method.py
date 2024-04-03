

def euler_method(f, x0, y0, h, n):
    # f: function dy/dx = f(x, y)
    # x0: initial value of x
    # y0: initial value of y
    # h: step size
    # n: number of steps
    
    x = x0
    y = y0
    for _ in range(n):
        y = y + h * f(x, y)
        x = x + h
    return y