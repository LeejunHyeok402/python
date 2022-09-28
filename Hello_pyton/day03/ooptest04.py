class Byden:
    def __init__(self):
        self.acd = 10
        
    def makewar(self):
        self.acd -= 1
    
class Putin:
    def __init__(self):
        self.nuclear = 6666
    
    def altzheimer(self):
        self.nuclear -= 1
        
class Mugun(Byden,Putin):
    def __init__(self):
        Putin.__init__(self)
        Byden.__init__(self)
        
m = Mugun()
print(m.nuclear)
print(m.acd)
m.makewar()
m.altzheimer()
print(m.nuclear)
print(m.acd)