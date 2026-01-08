def f(word):
    i=0
    result= ''
    while i<len(word):
        result += word[0:i] + word[i].upper() + word[i+1:len(word)]
        if i<len(word)-1:
            result += '-'
        i+=1
    return result


print(f('ware'))
