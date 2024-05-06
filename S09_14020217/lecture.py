###############################################
################# Inheritance #################
###############################################

class Person:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age


class Employees(Person):
    def __init__(self, id, name, age, role, salary):
        super().__init__(id, name, age)
        self.role = role
        self.salary = salary
    
    @classmethod    
    def getting_details(cls):
        name = input("enter your name : ")
        id = input("enter your id : ")
        age = input("enter your age : ")
        role = input("enter your role : ")
        salary = input("enter your salary : ")
        return cls(id, name, age, role, salary)
    def __str__(self):
        pass

selectedEmploye = Employees.getting_details()
print(selectedEmploye)

################################################
################# Polymorphism #################
################################################

class Transportation:
    def __init__(self, count_of_wheels, avg_speed, mpg, hp):
        self.count_of_wheels = count_of_wheels
        self.avg_speed = avg_speed
        self.mpg = mpg
        self.hp = hp

class Car(Transportation):
    def __init__(self, count_of_wheels, avg_speed, mpg, hp, count_of_doors, zero_to_hundret, car_type):
        super().__init__(count_of_wheels, avg_speed, mpg, hp)
        self.count_of_doors = count_of_doors
        self.zero_to_hundret = zero_to_hundret
        self.car_type = car_type

class Motocycle(Transportation):
    def __init__(self, count_of_wheels, avg_speed, mpg, hp, zero_to_hundret, motorcycle_type):
        super().__init__(count_of_wheels, avg_speed, mpg, hp)
        self.zero_to_hundret = zero_to_hundret
        self.motorcycle_type = motorcycle_type


class Airplane(Transportation):
    def __init__(self, count_of_wheels, avg_speed, mpg, hp, attitude, count_of_passenger):
        super().__init__(count_of_wheels, avg_speed, mpg, hp)
        self.attitude = attitude
        self.count_of_passenger = count_of_passenger

