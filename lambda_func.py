alpha = lambda x: x + 1
beta = lambda x: 2 * x

cero = lambda f: lambda a: a
uno = lambda f: lambda a: f(a)
dos = lambda f: lambda a: f(f(a))
tres = lambda f: lambda a: f(f(f(a)))
sucesor = lambda n: lambda f: lambda x: f(n(f)(x))
suma = lambda a: lambda b: lambda f: lambda x: a(f)(b(f)(x))
multiplicacion = lambda a: lambda b: lambda f: lambda x: a(b(f))(x)
potencia = lambda a: lambda b: lambda f: lambda x: b(a)(f)(x)



