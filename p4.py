def f(fnc,res):
    li = list(filter(fnc,res))
    return max(li)-min(li)

res = [95,90,20,50,70]
fnc1 = lambda x: x>50
print(f(fnc1,res))# returns 25
fnc2 = lambda x: x>30 and x<90
print(f(fnc2,res))# returns 20
