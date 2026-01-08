def f(uid):
    s = set()
    for i in uid:
        s.add(i)
    if len(s) !=len(uid):
        return False
    else:
        return True
    

print(f(["john5","ann123","JOHN5","xxx","abc333","a10"]))# returns True
print(f(["abc123","ann","abc123","a10"]))# returns False