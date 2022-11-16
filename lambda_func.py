alpha = lambda x: x + 1
beta = lambda x: 2 * x

cero = lambda f, x: x
uno = lambda f, x: f(x)
dos = lambda f, x: f(f(x))
tres = lambda f, x: f(f(f(x)))

'''def cero(f, x):
    return lambda f, x: x

def uno(f, x):
    return lambda f, x: f(x)

def dos(f, x):
    return lambda f, x: f(f(x))

def tres(f, x):
    return lambda f, x: f(f(f(x)))

def suma(a, b, f, x):
    return lambda a, b, f, x: a(f(b(f(x))))

def sucesor(n):
    return lambda a: a + n'''

