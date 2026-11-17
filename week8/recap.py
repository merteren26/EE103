from math import sqrt


def estimate_derivative(func, x, h=1e-5):
    return (func(x + h) - func(x - h)) / (2 * h)


def take_square(x):
    return x ** 2


def integrate(func, steps=1000):
    total_area = 0
    dx = 1 / steps
    for i in range(steps):
        midpoint = (i + 0.5) * dx
        total_area += func(midpoint) * dx
    return total_area


def f_x_twice(x, f_x):
    return f_x(f_x(x))


square_lambda = lambda x: x ** 2


if __name__ == "__main__":
    x = 3
    print(estimate_derivative(take_square, x))
    print(estimate_derivative(square_lambda, x))
    print(integrate(take_square))
    print(f_x_twice(16, sqrt))
    print(f_x_twice(2, square_lambda))