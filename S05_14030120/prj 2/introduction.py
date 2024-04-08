class Human:
    def __init__(self, name, age, job):
       self.name = name
       self.age = age
       self.job = job

    def __str__(self):
        return f"{self.name} and {self.job}"
    
    def DateOfBirth(self): #Method
        return (2024 - self.age)
    

p3 = Human("Parsa", 20, "Student")
print(p3.DateOfBirth())

