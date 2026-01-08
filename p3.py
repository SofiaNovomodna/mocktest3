def  f(d):
    tot =0
    cou =0
    count =0
    for key, value in d.items():
        tot += value
        cou +=1
    av = tot/cou
    for key, value in d.items():
        if value > av:
            count +=1

    return count

print(f({"LO231":150,"BA787":120,"NZ15":30}))# returns 2
print(f({"LO231":150,"BA787":20,"NZ15":30}))# returns 1