#2ai)
class Vehicle:
    def __init__(self,ID,Maxspeed,IncreaseAmount):
        self.__ID = ID #string
        self.__MaxSpeed = Maxspeed #integer
        self.__IncreaseAmount = IncreaseAmount #integer
        self.__CurrentSpeed = 0 #integer
        self.__HorizontalPosition = 0 #integer

    #2aii)
    def GetCurrentSpeed(self):
        return self.__CurrentSpeed
    
    def GetIncreaseAmount(self):
        return self.__IncreaseAmount
    
    def GetHorizontalPosition(self):
        return self.__HorizontalPosition
    
    def GetMaxSpeed(self):
        return self.__MaxSpeed

    #2aiii)
    def SetCurrentSpeed(self,newspeed):
        self.__CurrentSpeed = newspeed

    def SetHorizontalPosition(self,newpos):
        self.__HorizontalPosition = newpos

    #2aiv)
    def IncreaseSpeed(self):
        newspeed = self.__CurrentSpeed + self.__IncreaseAmount
        if self.__MaxSpeed > newspeed:
            self.__CurrentSpeed = newspeed
        else:
            self.__CurrentSpeed = self.__MaxSpeed
        
        self.__HorizontalPosition += self.__CurrentSpeed


#2bi)
class Helicopter(Vehicle):
    
    def __init__(self, ID, Maxspeed, IncreaseAmount, VerticalChange, MaxHieght):
        super().__init__(ID, Maxspeed, IncreaseAmount)
        self.__VerticalChange = VerticalChange #integer
        self.__MaxHieght = MaxHieght #integer
        self.__VerticalPosition = 0 #integer
    
    #2bii)
    def IncreaseSpeed(self):
        currentspeed = self.GetCurrentSpeed() 
        increaseamount = self.GetIncreaseAmount()
        newspeed = currentspeed + increaseamount
        newpos = self.__VerticalPosition + self.__VerticalChange
        
        if self.GetMaxSpeed() > newspeed:
            self.SetCurrentSpeed(newspeed)
        else:
            self.SetCurrentSpeed(self.GetMaxSpeed)
        
        self.SetHorizontalPosition(self.GetHorizontalPosition()+self.GetCurrentSpeed()) 

        if self.__MaxHieght > newpos:
            self.__VerticalPosition = newpos
        else:
            self.__VerticalPosition = self.__MaxHieght

    #2c)
    def GetVerticalPosition(self):
        return self.__VerticalPosition


#2c)
def Outputdata(object):
    if isinstance(object, Vehicle):   
        print(f"Horizontal position: {object.GetHorizontalPosition()}")
        print(f"Speed: {object.GetCurrentSpeed()}")
    if isinstance(object, Helicopter):
        print(f"Vertical position: {object.GetVerticalPosition()}")

car1 = Vehicle('Tiger',100,20)
helicopter1 = Helicopter('Lion',350,40,3,100)
car1.IncreaseSpeed()
car1.IncreaseSpeed()
Outputdata(car1)
helicopter1.IncreaseSpeed()
helicopter1.IncreaseSpeed()
Outputdata(helicopter1)