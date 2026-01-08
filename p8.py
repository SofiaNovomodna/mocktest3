def f(fnc,prods):
    l4= list(map(fnc,prods))
    i=0
    result = ''
    while i<len(l4):
        result += l4[i]
        if i<len(l4)-1:
            result += ','
        i+=1

    return result

prods = ["water","cheese","tomato"]
fnc1 = lambda x: "id:"+x[:2]
print(f(fnc1,prods)) #returns "id:wa,id:ch,id:to"
fnc2 = lambda x: (x[0]+x[-1]).upper()
print(f(fnc2,prods))# returns "WR,CE,TO"

