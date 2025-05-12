Animal = ["" for i in range(20)]
Colour = ["" for i in range(10)]
AnimalTopPointer = 0
ColourTopPointer = 0

def PushAnimal(DataToPush:str) -> bool:
    global AnimalTopPointer
    if AnimalTopPointer == 20:
        return False
    else:
        Animal[AnimalTopPointer] = DataToPush
        AnimalTopPointer = AnimalTopPointer + 1
        return True
    
def PushColour(DataToPush:str) -> bool:
    global ColourTopPointer
    if ColourTopPointer == 20:
        return False
    else:
        Colour[ColourTopPointer] = DataToPush
        ColourTopPointer = ColourTopPointer + 1
        return True

def PopAnimal():
    global AnimalTopPointer
    ReturnData = ""
    if AnimalTopPointer == 0:
        return ""
    else:
        ReturnData = Animal[AnimalTopPointer-1]
        AnimalTopPointer = AnimalTopPointer - 1
        return ReturnData
    
def PopColour():
    global ColourTopPointer
    ReturnData = ""
    if ColourTopPointer == 0:
        return ""
    else:
        ReturnData = Colour[ColourTopPointer-1]
        ColourTopPointer = ColourTopPointer - 1
        return ReturnData

def OutputItem():
    global AnimalTopPointer
    global ColourTopPointer
    CurrentAnimal = PopAnimal()
    CurrentColour = PopColour()
    if AnimalTopPointer != 0 and ColourTopPointer != 0:
        print("{} {}".format(CurrentColour,CurrentAnimal))
    if AnimalTopPointer == 0:
        print("No animal")
    if ColourTopPointer == 0:
        print("No colour")

def ReadData():
    f = open("AnimalData.txt","r")
    for i in f:
        PushAnimal(i.strip())
    f.close()
    f2 = open("ColourData.txt","r")
    for i in f2:
        PushColour(i.strip())
    f2.close()

ReadData()
OutputItem()
OutputItem()
OutputItem()
OutputItem()