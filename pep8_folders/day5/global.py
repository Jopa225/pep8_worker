globalna = 5
def foo():
    globalna = 6
    print(globalna) 

def foo1():
    global globalna
    globalna = 2

def foo2(globalna):
    globalna = 9
    return globalna

foo()
print(globalna)

foo1()
print(globalna)
globalna = foo2(globalna)
print(globalna)