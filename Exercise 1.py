y = 0
name = {}

name["John"] = [6*2,8,7]
name["Tom"] = [5*2,9,10]
name["Jerry"] = [8*2,6,5]
x = str(input("Student name: "))
print(name[x])

for element in range(0, len(name[x])):
    y = (y + name[x][element])

avg = y/4
print("The average grade of this student is:" ,avg) 

if avg>=8 and avg<=10:
    print("Diamond")
elif avg>=7 and avg <8:
    print("Gold")
elif avg>=5 and avg<7:
    print("Silver")
elif avg>=0 and avg<5:
    print("Copper")
else:
    print("Invalid")
