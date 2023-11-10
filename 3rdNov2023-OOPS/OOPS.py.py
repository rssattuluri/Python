# Class and Object in Python.

# Person
# Attributes - name,age, phone_no, height, weight, gender, prof
# Methods - Can do -> Run(), sleep(). sing(), talk(), eat(), fight(), learn(), hear(), think()


# Objects
# Amit
# Durga - GENDER  - fEMALE
# Santosh -

class Person:
    # Attributes
    name = None
    age = None
    phone_no = None
    height = None
    weight = None
    gender = None
    prof = None

    # Methods
    def talk(self):
        print("Talk")

    def sleep(self):
        print("Sleep")

    def walk(self):
        return "I am walking"


amit_object = Person()
amit_object.name = "Amit"
amit_object.age = 59
amit_object.phone_no = "987654321"

print(amit_object)
amit_object.sleep()

durga_obj = Person()
durga_obj.name = "Durga"

print(durga_obj)
durga_obj.sleep()

# Car -
# Objects - Tesla, Lambo

class Car:
    name = None
    color = None
    model = None
    speed = None
    engine = None

# self is a special variable that is used within the context of
# object-oriented programming (OOP).
# It is a reference to the instance of a class
# access and manipulate the attributes and methods of that instance / Object


    def start_engine(self):
        print("Starting engine")

    def drive(self):
        print("Drive")

    def car_break(self):
        print("Break")

    def who_is_driving(self):
        print("I am driving -> " +  self.name)


tesla_obj_ref  = Car() # This is instance of a Class - Object
lambo_obj_ref = Car() # This is instance of a Class - Object

tesla_obj_ref.name =  "Tesla"
lambo_obj_ref.name = "Lambo"


tesla_obj_ref.who_is_driving()
lambo_obj_ref.who_is_driving()



def sum(a,b):
    return a+b

# Function?


sum(3,4)

class P:
    def m1(self):
        print("Method")


# m1()

class Myclass:

    def print_my_name_with_last_name(self,name, last_name, age):
        print("You name is -> " + name, last_name, age)


pramod_obj_ref = Myclass()
pramod_obj_ref.print_my_name_with_last_name("Amit", "dutta", 34)



# Take a input from user we will create How

class Car:
    color = None
    model = None

    def car_details(self):
        print("Your car details is ", self.color, self.model)

car_color = input("Enter you car Color")
car_model = input("Enter you car Model")

car_obj_ref = Car()
car_obj_ref.color = car_color
car_obj_ref.model = car_model

# Obj ref we can call the function
car_obj_ref.car_details()

# car_details()