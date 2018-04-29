class Home:
            def __init__(self,area):
                self.area = area;
                self.rongNaList = []
            def __str__(self):
                msg= "current area is "+str(self.area)
                return msg
            def containItem(self, item):
                bedArea = item.getBedArea()
                if self.area>bedArea:
                    self.rongNaList.append(item)
                    self.area -= bedArea
                    print "add success current space is " + str(self.area)
                else:
                    print("not enough space")

class Bed:
         def __init__(self, name, area):
            self.area = area;
            self.name = name;
         def __str__(self):
            msg = self.name + " is account for "+ str(self.area)
            return msg
         def getBedArea(self):
            return self.area
        
home = Home(180)
print(home)
bed = Bed("ximengsi",4)
print(bed)
bed2 = Bed("muban",120)
home.containItem(bed)
home.containItem(bed2)
print(home)