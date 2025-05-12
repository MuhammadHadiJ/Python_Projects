class Vehicle:
    def __init__(self, ID, MaxSpeed, IncreaseAmount):
        self.__ID = ID
        self.__MaxSpeed = MaxSpeed
        self.__IncreaseAmount = IncreaseAmount
        self.__CurrentSpeed = 0
        self.__HorizontalPosition = 0

    def GetCurrentSpeed(self):
        return self.__CurrentSpeed
    
    def GetIncreaseAmount(self):
        return self.__IncreaseAmount
    
    def GetHorizontalPosition(self):
        return self.__HorizontalPosition
    
    def GetMaxSpeed(self):
        return self.__MaxSpeed
    
    def SetCurrentSpeed(self, CurrentSpeed):
        self.__CurrentSpeed = CurrentSpeed
    
    def SetHorizontalPosition(self, HorizontalPosition):
        self.__HorizontalPosition = HorizontalPosition

    def IncreaseSpeed(self):
        if self.__CurrentSpeed + self.__IncreaseAmount < self.__MaxSpeed:
            self.__CurrentSpeed = self.__CurrentSpeed + self.__IncreaseAmount
            self.__HorizontalPosition = self.__HorizontalPosition + self.__CurrentSpeed
        else:
            self.__CurrentSpeed = self.__MaxSpeed
            self.__HorizontalPosition = self.__HorizontalPosition + self.__CurrentSpeed

    def GetHorizontalPosAndSpeed(self):
        print("The horizontal position of the vehicle is {} and the speed is {}".format(self.__HorizontalPosition,self.__CurrentSpeed))

class Helicopter(Vehicle):
    def __init__(self, ID, MaxSpeed, IncreaseAmount, VerticalChange, MaximumHeight):
        super().__init__(ID, MaxSpeed, IncreaseAmount)
        self.__VerticalPosition = 0
        self.__VerticalChange = VerticalChange
        self.__MaximumHeight = MaximumHeight
        self.__CurrentSpeed = self.GetCurrentSpeed() 
        self.__IncreaseAmount = self.GetIncreaseAmount()
        self.__MaxSpeed = self.GetMaxSpeed()
        self.__HorizontalPosition = self.GetHorizontalPosition()
    
    def IncreaseSpeed(self):
        if self.__VerticalPosition + self.__VerticalChange < self.__MaximumHeight:
            self.__VerticalPosition = self.__VerticalPosition + self.__VerticalChange
        elif self.__VerticalPosition + self.__VerticalChange > self.__MaximumHeight:
            self.__VerticalPosition = self.__MaximumHeight
        if self.__CurrentSpeed + self.__IncreaseAmount < self.__MaxSpeed:
            self.__CurrentSpeed += self.__IncreaseAmount
        elif self.__CurrentSpeed + self.__IncreaseAmount > self.__MaxSpeed:
            self.__CurrentSpeed = self.__MaxSpeed
        self.__HorizontalPosition += self.__CurrentSpeed

    def GetHorizontalPosAndSpeed(self):
        print("The horizontal position of the vehicle is {}, the speed is {} and the vertical position is {}".format(self.__HorizontalPosition,self.__CurrentSpeed,self.__VerticalPosition))

Car = Vehicle("Tiger",100,20)
Car.IncreaseSpeed()
Car.IncreaseSpeed()
Car.GetHorizontalPosAndSpeed()
Heli = Helicopter("Lion",350,40,3,100)
Heli.IncreaseSpeed()
Heli.IncreaseSpeed()
Heli.GetHorizontalPosAndSpeed()