alpha = lambda x: x + 1
beta = lambda x: 2 * x

def cero(f, x):
    return lambda f, x: x

def uno(f, x):
    return lambda f, x: f(x)

def dos(f, x):
    return lambda f, x: f(f(x))

def tres(f, x):
    return lambda f, x: f(f(f(x)))

def suma(a, b):
    return lambda a, b: a + b

def sucesor(n):
    return lambda a: a + n

