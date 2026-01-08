def f(mnumbers):
    import re
    pat = '^[+-]?[A-Da-d1-7]+$'
    list3 = []
    for i in mnumbers:
        ch = re.match(pat,i)
        if ch != None:
            list3.append(i)

    return len(list3)

print(f(["A15","-31","7abC","+D1","-g4"]))# returns 4
print(f(["A05","-3+1","7ab8C","+Bb7","-22c55"]))# returns 2