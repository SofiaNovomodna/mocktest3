def f(value1):
    return lambda value2: value2* value1
    
times_five = f(5)
print(times_five(8))# returns 40
times_three = f(3)
print(times_three(7))# returns 21