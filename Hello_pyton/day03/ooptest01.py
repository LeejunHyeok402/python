class Animal:
    
    def __init__(self):
        self.hungry = 5
    
    def timegoby(self):
        if self.hungry > 0:
            self.hungry -= 1
            
    def mattang(self):
        self.hungry = 10
        
# ani = Animal()
# print(ani.hungry)
# ani.timegoby()
# ani.mattang()
# print(ani.hungry)

class Human(Animal):
    
    def __init__(self):
        super().__init__()
        self.skill_lang = 0
    
    def momstouch(self,stroke):
        self.skill_lang += stroke
        
h = Human()
print(h.hungry)
print(h.skill_lang)
h.mattang()
h.momstouch(11)
print(h.hungry)
print(h.skill_lang)