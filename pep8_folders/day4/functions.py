def func1():
    print("func1")  
func1()

def func2(a,b):
    return a+b
print(func2(1,2))

def func3(a, b, c=2, d=4):
    return a+b+c+d
print(func3(1,2))
print(func3(1,2,3))
print(func3(1,2,3,5))

def func_args(*args):
    result = 0
    for argument in args:
        result += argument
    return result
suma = func_args(10,10,10,10,10)
print(suma)

def func_callback(callback, *args):
    return callback(*args)
print(func_callback(func_args,10,10,1,1,1,1,1,1,10))



