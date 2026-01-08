def f(date):
    import re
    pat = '^\d{4}-\d{2}-\d{2}$'
    l2 = []
    date_list = date.split(',')
    for i in date_list:
        ch = re.match(pat,i)
        if ch != None:
            l2.append(i)
    return l2

dates = "2021-1-3, 05/12/2024, 1998-12-11, 9 maj 2007, 2001-12-07, 15-09-2011"

print(f(dates))# returns ["1998-12-11","2001-12-07"]
