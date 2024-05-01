from os import system

# Class Name -> Pascal Case

class Student:
    courses = []
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def AddCourses(self, course_name):
        self.courses.append([course_name, 0])

    def AddCoursesPoint(self, course_name, course_point):
        for index, course in enumerate(self.courses):
            if course[0] == course_name:
                self.courses[index] = [course_name, course_point]


    def ShowCourses(self):
        return self.courses

    def CalculateSemster(self):
        sum = 0
        count = len(self.courses)
        avg = 0

        for course in self.courses:
            sum += int(course[1])

        avg = sum / count

        if avg >= 10:
            return f"Student pass with {avg} GPA"
        
        else:
            return f"Student didn't pass with {avg} GPA"


std1 = Student("Parsa", "Salimi")

flag = True
while flag:
    system("cls")
    print(std1.ShowCourses())
    answer = input("1. Add Course\n2. Add Course Point\n3. Calculate the Semester\n> ")
    if answer == "1":
        course_name = input("What's the Course name: ")
        std1.AddCourses(course_name)

    elif answer == "2":
        course_name = input("What's the Course name: ")
        course_point = input("What's the Score: ")
        print(std1.AddCoursesPoint(course_name,course_point))

    elif answer == "3":
        std1.CalculateSemster()
        input()