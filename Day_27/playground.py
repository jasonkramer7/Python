def add(*args):
    return sum(args)


print(add(4, 5, 6, 5))


def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiple"]
    print(n)


calculate(2, add=3, multiple=5)
