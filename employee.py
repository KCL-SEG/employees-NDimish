"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, typepay,baserate,hour, contract,bonusrate):
        self.name = name
        self.typepay = typepay
        self.baserate = baserate
        self.hour = hour
        self.contract = contract
        self.bonusrate = bonusrate

    def get_pay(self):
            if(self.typepay == 1):
                 return self.baserate
            if(self.typepay == 2):
                 return self.baserate*self.hour
            if(self.typepay == 3):
                 return self.baserate+(self.contract*self.bonusrate)
            if(self.typepay == 4):
                 return (self.baserate*self.hour)+(self.contract*self.bonusrate)
            if(self.typepay == 5):
                 return self.baserate+self.bonusrate
            if(self.typepay == 6):
                 return (self.baserate*self.hour)+ self.bonusrate   
            else:
                return 0

    def __str__(self):
            if(self.typepay == 1):
                 return self.name +" works on a monthly salary of " +self.baserate+". Their total pay is "+self.get_pay+"."
            if(self.typepay == 2):
                 return self.name + " works on a contract of "+self.hour+" hours at "+self.baserate+"/hour.  Their total pay is "+self.get_pay+"."
            if(self.typepay == 3):
                 return self.name+" works on a monthly salary of "+self.baserate+" and receives a commission for "+self.contract+" contract(s) at "+self.bonusrate+"/contract.  Their total pay is "+self.get_pay+"."
            if(self.typepay == 4):
                 return self.name+" works on a contract of "+self.hour+" hours at "+self.baserate+"/hour and receives a commission for "+self.contract+" contract(s) at "+self.bonusrate+"/contract.  Their total pay is "+self.get_pay+"."
            if(self.typepay == 5):
                 return self.name+ " works on a monthly salary of "+self.baserate+" and receives a bonus commission of "+self.bonusrate+".  Their total pay is "+self.get_pay+"."
            if(self.typepay == 6):
                 return self.name+" works on a contract of "+self.hour+" hours at "+self.baserate+"/hour and receives a bonus commission of "+self.bonusrate+".  Their total pay is "+self.get_pay+"."    
            else:
                return "error"


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie',1,4000,0,0,0)
# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie',2,25,100,0,0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee',3,3000,0,4,200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan',4,25,150,3,220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie',5,2000,0,0,1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel',6,30,120,0,600)
