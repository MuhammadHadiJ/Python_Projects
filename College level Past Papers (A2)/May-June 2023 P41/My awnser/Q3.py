#3ai)
global Animal  #array of string with 20 spaces
global Colour  #array of string with 10 spaces
global AnimalTopPointer  #integer
global ColourTopPointer #integer
Animal = ['' for i in range(20)]
Colour = ['' for i in range(10)]
AnimalTopPointer = 0
ColourTopPointer = 0

#3bi)
def PushAnimal(DataToPush):
    global Animal
    global AnimalTopPointer
    
    if AnimalTopPointer == 20:
        return False
    else:
        Animal[AnimalTopPointer] = DataToPush
        AnimalTopPointer = AnimalTopPointer + 1
        return True

#3bii)   
def PopAnimal():
    global Animal
    global AnimalTopPointer
    
    Returndata = ""
    if AnimalTopPointer == 0:
        return ""
    else:
        Returndata = Animal[AnimalTopPointer-1]
        AnimalTopPointer = AnimalTopPointer -1
        return Returndata

#3biv)
def PushColour(DataToPush):
    global Colour
    global ColourTopPointer

    if ColourTopPointer == 10:
        return False
    else:
        Colour[ColourTopPointer] = DataToPush
        ColourTopPointer = ColourTopPointer + 1
        return True

  
def PopColour():
    global Colour
    global ColourTopPointer
    
    Returncdata = ""
    if ColourTopPointer == 0:
        return ""
    else:
        Returncdata = Colour[ColourTopPointer-1]
        ColourTopPointer = ColourTopPointer -1
        return Returncdata

#3biii)
def ReadData():
    global Animal
    global Colour
    global AnimalTopPointer
    global ColourTopPointer
    
    try:
        with open('AnimalData.txt','r') as file:
            for name in file:
                PushAnimal(name.strip())
    except FileNotFoundError:
        print("File does not exist")
    
    #3bv)
    try:
        with open('ColourData.txt','r') as file2:
            for clr in file2:
                PushColour(clr.strip())
    except FileNotFoundError:
        print("File does not exist")


#3c)
def OutputItem():
    data1 = PopAnimal()
    data2 = PopColour()
    
    if data1 == "":
        PushColour(data2)
        print("No animal")
    
    if data2 == "":
        PushAnimal(data1)
        print("No colour")

    if data1!="" and data2!="":
        print(data2 + " " + data1)

ReadData()
OutputItem()
OutputItem()
OutputItem()
OutputItem()