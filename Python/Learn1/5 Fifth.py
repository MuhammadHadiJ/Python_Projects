weight = float(input("weight: "))
weight2 = input("(k)g or (L)bs ")
if weight2.upper() == "L":
    converted = weight * 0.45
    print("weight in kg:" + str(converted))
else:
    converted = weight / 0.45
    print("weight in lbs:" + str(converted))