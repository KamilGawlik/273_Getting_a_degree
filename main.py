pi = 3.1415926536
ninefive = 9/5
fivenine = 5/9

def rtod(number):
    degrees = number*180/pi
    print(number, "r = ", int(degrees), "d")

def dtor(number):
    radians = number * pi / 180
    print(number, "d = ", radians, "r")

def ctof(number):
    farenheit = number * ninefive + 32
    print(number, "c = ", farenheit, "f")

def ctok(number):
    kelvin = number + 273.15
    print(number, "c = ", kelvin, "r")

def ftoc(number):
    celcius = (number - 32) * fivenine
    print(number, "f = ", celcius, "c")

def ftok(number):
    kelvin = (number + 459.67) * fivenine
    print(number, "f = ", round(kelvin, 2), "k")

def ktof(number):
    farenheit = number * ninefive - 459.67
    print(number, "k = ", farenheit, "f")

def ktoc(number):
    celcius = number - 273.15
    print(number, "k = ", round(celcius, 2), "c")

string = input()
try:
    number = float(string[:-2])
    convertfrom = str(string[-2])
    convertto = str(string[-1])


    if convertfrom == "r" or convertfrom == "d":
            if convertfrom == "r":
                if convertto == "d":
                    rtod(number)
                else:
                    print("No candidate for conversion")
            if convertfrom == "d":
                if convertto == "r":
                    dtor(number)
                else:
                    print("No candidate for conversion")
    elif convertfrom == "c" or convertfrom == "f" or convertfrom == "k":
        if convertfrom == "c":
            if convertto == "f":
                ctof(number)
            elif convertto == "k":
                ctok(number)
            else:
                print("No candidate for conversion")
        elif convertfrom == "f":
            if convertto == "c":
                ftoc(number)
            elif convertto == "k":
                ftok(number)
            else:
                print("No candidate for conversion")
        elif convertfrom == "k":
            if convertto == "f":
                ktof(number)
            elif convertto == "c":
                ktoc(number)
            else:
                print("No candidate for conversion")
except:
    print("Invalid input")