# Adapt Light class in order to overload operator for addition:
# + operator creates new instance (new_object) of the Light class
# new_object will have type of concatenated types of summarized objects
# For Light, Headlight and Left_Blinkers, both classes and instances, check all relations who is subclass of who, using builtin
# functions, and list of all names from the symbol table (check slides for Modules).


class Light:
    "Light superclass"

    VIN = "prototype_vehicle"
    id = 0
    value = True
    type_of_light = ""

    def __init__(self, type_of_light):
        Light.id += 1
        self.id = Light.id
        self.type_of_light = type_of_light
    
    def get_id(self):
        print(f"Light type is {self.type_of_light}.Light id is {self.id}")
    
    def set_value(self, value):
        self.value = value
    
    def get_value(self):
        print(f"Status of light {self.value}")

    def __add__(self, other):
        return Light(self.type_of_light + " " + other.type_of_light)

class Headlight(Light):
    "Headlight subclass"
    bulb_type =""
    side = ""
    def __init__(self, type_of_light, bulb_type, side):
        super().__init__(type_of_light)
        self.bulb_type = bulb_type
        self.side = side
    
    def get_id(self):
        print("Not Door!")

class Blinkers(Headlight):


    def __init__(self, type_of_light, bulb_type, side, value=False):
        super().__init__(type_of_light, bulb_type, side)
        self.set_value(value)
    
left_blinkers = Blinkers("door","Xenon", "left", True)
left_blinkers.get_id()
left_blinkers.get_value()


Left_Headlight = Headlight("door","Xenon", "left")
Right_Headlight = Headlight("door","Xenon", "right")
Left_Headlight.set_value(True)
Right_Headlight.set_value(True)
Left_Headlight.get_id()
Right_Headlight.get_id()

Q = Light("door")
W = Light("door")
A = Light("door")
D = Light("door")
print(getattr(Q, "type_of_light"))
print(getattr(W, "type_of_light"))
setattr(Q, "type_of_light", "front_left")
setattr(W, "type_of_light", "front_right")
setattr(A, "type_of_light", "rear_left")
setattr(D, "type_of_light", "rear_right")

Q.get_id()
W.get_id()
A.get_id()
D.get_id()

Q.get_value()

print(isinstance(Q,Light))
print(isinstance(W,Light))
print(isinstance(A,Light))
print(isinstance(D,Light))
b = D + A
b.get_id()


print(issubclass(Headlight, Light))
print(issubclass(Blinkers, Headlight))
print(issubclass(Blinkers, Light))
print(issubclass(Light,Blinkers))
# print(issubclass(left_blinkers, Left_Headlight))

print(dir(b))
print(dir(Headlight))
print(dir(Blinkers))


