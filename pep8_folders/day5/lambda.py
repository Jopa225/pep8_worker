def foo(n):
    return lambda x: x**n

exp = foo(3)
print(exp(2))

