pi = 3.1415926536
def rtod(number):
    degrees = number*180/pi
    print(number, "radians are equal to ", int(degrees), " degrees")
def dtor(number):
    radians = number * pi / 180
    print(number, "degrees are equal to ", radians, " radians")
string = str(input("Podaj liczbe"))
number = float(string[:-2])
convertfrom = str(string[-2])
convertto = str(string[-1])



if convertfrom == "r":
    if convertto == "d":
        rtod(number)
if convertfrom == "d":
    if convertto == "r":
        dtor(number)