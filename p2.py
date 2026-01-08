class C:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def m1 (self):
        if self.x == 0 or self.y == 0:
            return 0
        if self.x>0:
            if self.y>0:
                return 1
            elif self.y<0:
                return 4
        if self.x<0:
            if self.y>0:
                return 2
            elif self.y<0:
                return 3
            
    def m2(self, a,b):
        if a == 0 or b == 0:
            check = 0
        if a>0:
            if b>0:
                check =  1
            elif b<0:
                check =  4
        if a<0:
            if b>0:
                check =  2
            elif b<0:
                check =  3
        
        if self.x == 0 or self.y == 0:
            check1 =  0
        if self.x>0:
            if self.y>0:
                check1 = 1
            elif self.y<0:
                check1 = 4
        if self.x<0:
            if self.y>0:
                check1 = 2
            elif self.y<0:
                check1 = 3
            

        if check == check1:
            return True
        else:
            return False
        
    def m3(self, a,b):
        import math
        e = (a-self.x)*(a-self.x) + (b-self.y)*(b-self.y)
        if math.sqrt(e) >5 :
            return True
        else: 
            return False
        

p = C(2,3)
print(p.m1() )#returns 1
print(p.m2(7,4)) #returns True
print(p.m2(-3,1) )#returns False
print(p.m3(8,5)) #returns True
print(p.m3(4,7)) #returns False
p1 = C(0,5)
print(p1.m1()) #returns 0
print(p1.m2(4,7) )#returns False
print(p1.m2(-7,0)) #returns True

