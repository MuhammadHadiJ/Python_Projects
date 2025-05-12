#Adjusted Start time 6:20
#1ai)
Dataarray = [] #array of type integer with 25 spaces 
#1aii)
with open('Data.txt','r') as file:
    for num in file:
        Dataarray.append(int(num.strip()))


#1bi)
def Printarray(intarray):
    i = 0
    data = ''
    
    while i < len(intarray):
        data = data + str(intarray[i]) + ' '
        i+=1
    
    print(data)

#1bii)
Printarray(Dataarray)

#1c)
def LinearSearch(intarray, searchvalue):
    i=0
    found = 0
    while i < len(intarray):
        if intarray[i] == searchvalue:
            found +=1
        i+=1
    return found

#1di)

isnum = False 
while isnum == False:
    number = int(input("Enter a number between 0 and 100: "))
    if number >= 0 and number <= 100:
        isnum = True
    else:
        print("Input a valid number")

result = LinearSearch(Dataarray,number)
print(f"The number {number} is found {result} times")