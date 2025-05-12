DataArray = []

with open("Data.txt", "r") as file:
    for i in file:
        DataArray.append(int(i.strip()))

def PrintArray(arr):
    arr2 = ""
    i = 0
    while i <= len(arr[0:-1]):
        arr2 = arr2 + str(arr[i]) + " "
        i = i + 1
    return arr2

def LinearSearch(arr, value):
    i = 0
    y = 0
    while i < len(arr):
        if int(arr[i]) == value:
            y = y + 1
        i = i + 1
    return "The number " + str(value) + " is found " + str(y) + " times"

print(PrintArray(DataArray))
InputedValue = input("Enter a whole number between 0 and 100 inclusive: ")
while int(InputedValue) > 100 or int(InputedValue) < 0:
    InputedValue = input("Enter a whole number between 0 and 100 inclusive: ")
print(LinearSearch(DataArray, int(InputedValue)))