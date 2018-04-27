class SweetPotato:
    def __init__(self):
        self.cooklevel =0
        self.cookedstate ="raw"
        self.condiments = []

    def __str__(self):
        msg = "your potato is in state :" +self.cookedstate
        if len(self.condiments)>0:
            msg+=" your source is: "
            for temp in self.condiments:
                msg  = msg + temp + ", "
             # remove the last ,
            msg = msg.strip(", ")
        return msg

    def cook(self,time):
        self.cooklevel += time
        if self.cooklevel>8:
            self.cookedstate = "too mature"
        elif self.cooklevel>5:
            self.cookedstate ="it is ok"
        elif self.cooklevel>3:
            self.cookedstate =" it is half raw half mature"
        else:  self.cookedstate =  "it is raw"

    def addcondiments(self, temp):
        self.condiments.append(temp)

digua = SweetPotato()
print(digua)
#print(digua.cooklevel)
#print(digua.cookedstate)
print "start cooking"
print"cook two minutes"
digua.cook(2)
#print digua.cookedstate
#print "two minutes left"
digua.cook(2)
#print digua.cookedstate
print(digua)
print "cook 3 minutes"
digua.cook(3)
digua.addcondiments("potato source")
digua.cook(5)
digua.addcondiments("blackbean source")
print(digua)