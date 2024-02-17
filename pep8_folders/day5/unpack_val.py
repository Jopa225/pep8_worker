def func1(x, *args):
    dicty = {}
    dicty["original"] = args
    for key in dicty.keys():
        dicty[key] = dicty[key]**2
    dicty["power_of"] = dicty[key]
    return dicty

def func2(original, power_of):
    return func1(2, original) + power_of

dict = func1(2,1,2,3)
print(dict)
print(func2(**dict))##########


