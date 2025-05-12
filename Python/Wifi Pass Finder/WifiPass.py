List1 = ["When", "Where", "How"]
List2 = ["What", "why"]
List1.extend(List2[:2])
List1.pop()
List1.sort()
Fullist = ""

for course in List1:
    print(List1.index(course)+1,course+"\n")

for num, course in enumerate(List1,start=1):
    print(num,course)

Fullist2 = ", ".join(List1)
print("\n"+Fullist2)

for Course in List1:
    if Course != List1[-1]:
        Fullist = Fullist + Course + ", "
    else:
        Fullist = Fullist + Course
print(Fullist)

    