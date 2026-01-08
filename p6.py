class C:
    def __init__(self, fn, ln, a):
        self.fn = fn
        self.ln = ln
        self.a = a

    def __str__(self):
        if self.a >=18:
            result = self.fn[0].upper() + self.ln[0].upper() + str(self.a)
        else:
            result = self.fn[0].lower() + self.ln[0].lower() + str(self.a)
        return result
        



print(C("John","May",21))# returns "JM21"
print(C("Anna","Brown",17))# returns "ab17"