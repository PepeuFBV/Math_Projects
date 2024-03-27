def gaussian_quadrature(f, a, b):
    # Gaussian quadrature for n=1 (third degree polynomial)
    
    x1 = -0.57735026919  # -sqrt(3)/3
    x2 = 0.57735026919   # sqrt(3)/3
    w1 = 1.0             # weight 1
    w2 = 1.0             # weight 2

    # map points from [-1, 1] to [a, b]
    x1 = ((b - a) * x1 + (b + a)) / 2
    x2 = ((b - a) * x2 + (b + a)) / 2

    integral_approximation = (w1 * f(x1) + w2 * f(x2)) * (b - a) / 2
    return integral_approximation