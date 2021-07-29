class Vehicle:
    def general_usage(self):
        print("general use: transportation")

class Car(Vehicle):
    def __init__(self):
        print("i'm car")
        
        self.wheels = 4
        self.has_roof = True
        self.general_usage()

    def specific_usage(self):
        self.general_usage()
        print("specific use: commute to work, vacation with family .", "wheel is: ",self.wheels) 



class MotorCycle(Vehicle):
    def __init__(self):
        print("i'm motorcycle")
        self.wheels = 2
        self.has_roof = False
        self.general_usage()

    def specific_usage(self):
        print("specific use: road trip, racing ")


c = Car()
print("is it instance ?: ",isinstance(c, Car))
print("car is a sub class ? :", issubclass(Car, Vehicle))
print("car is a sub class of motorcycle ? :", issubclass(Car, MotorCycle))
# c.general_usage() 
# c.specific_usage()      
M = MotorCycle()
M.specific_usage()
