#object oriented programming

#class is like declaration of type in python
class Car: #Car is a class - class names with capital
    def __init__(self, make, model, colour): #initialise and write the constructor
        self.make = make #differentiate it
        self.model = model
        self.colour = colour
    def start(self): #it calls itself
        print ("The car has started.")
    def stop(self):
        print ("The car has stopped")

#similar to RECORD data type (not possible on python tho)

 #declaring that car1 use Car data type
car1 = Car("Ferrari", "SF90", "Red")
#instantiation : to make an instance of a class


print(car1.start()) #print the fucntion

car2  = Car("Wuling", "Mini", "Yellow")
car3 = Car("Toyota","2001","Black")
print(car1.make)