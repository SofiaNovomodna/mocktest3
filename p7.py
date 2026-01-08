class C:
    def __init__(self, val):
        self.val = val

    def m1(self):
        return self.val

    def m2(self):
        self.val +=1

    def m3(self):
        self.val -=1

    def m4(self,n):
        self.val +=n

    def __str__(self):
        return str(self.val)
    

c=C(5)
print(c.m1())# returns 5
c.m2()
print(c.m1())# returns 6
c.m4(-8)
print(c.m1())# returns -2
c.m3()
print(c.m1())# returns -3
c.m4(10)
print(c.m1())# returns 7
print(c.__str__())# returns "7"
print(type(c.__str__()))