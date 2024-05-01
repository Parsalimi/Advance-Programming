class Student:
    def __init__(self, name):
        self.name = name
        
    def courses(self, course_one, course_two):
        self.course_one = course_one
        self.course_two = course_two
    
    def semester(self, semester_num):
        self.semester_num = semester_num
        if ((self.course_one + self.course_two) / 2) >= 10:
            self.semester_num += 1
        return self.semester_num
    
mehryar = Student("mehryar")
mehryar.courses(12, 14)
print(mehryar.semester(2))