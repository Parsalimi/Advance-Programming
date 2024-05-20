from tools import *
from student import Student

class Managment:
    def StudentID():
        with open("S11_midterm\\DB\\last_login_id.txt","r") as file:
            lastStudentId = file.read()
            if lastStudentId != "":
                lastStudentId = int(lastStudentId) + 1
                return lastStudentId
            else:
                return 1
            
    def UpdateLastStudentID():
        lastStudentId = Managment.StudentID()
        with open("midterm\DB\\last_login_id.txt","w") as file:
            file.write(str(lastStudentId))
            
    def AddStudent():
        ClearTerminal()
        print(ColoredNotification("Add Student", "green"))
        name = input("Enter Student Name: ")
        age = input("Enter Student Age: ")
        major = input("Enter Student Major: ")
        selectedStudent = Student(Managment.StudentID(),name, age, major)
        with open("S11_midterm\\DB\\students.txt","a") as file:
            file.write(f"{selectedStudent.__dict__}\n")
            file.close()
        Managment.UpdateLastStudentID()

    def ShowStudents():
        ClearTerminal()
        print(ColoredNotification("Student List", "green"))
        with open("S11_midterm\\DB\\students.txt","r") as file:
            for line in file.readlines():
                currentStudentDict = eval(line)
                selectedStudent = Student(currentStudentDict['id'],currentStudentDict['name'],currentStudentDict['age'],currentStudentDict['major'])
                print(f"{selectedStudent.id} | {TextStructure(selectedStudent.name,20)}| {selectedStudent.age} | {selectedStudent.major}")

    studentsList = []

    def UpdateStudentsList():
        Managment.studentsList = []
        with open("S11_midterm\\DB\\students.txt","r") as file:
            for line in file.readlines():
                Managment.studentsList.append(eval(line))

    def UpdateStudentsTxt():
        with open("S11_midterm\\DB\\students.txt","w") as file:
            for student in Managment.studentsList:
                file.writelines(f"{student}\n")

    
    def SearchStudent():
        ClearTerminal()
        Managment.UpdateStudentsList()
        print(ColoredNotification("Search Student", "green"))
        studentId = input("Please Enter the Student ID: ")
        userFounded = False
        for student in Managment.studentsList:
            if student['id'] == int(studentId):
                print(f"Student ID: {student['id']} | Name: {student['name']} | Age: {student['age']} | Major: {student['major']}")
                userFounded = True
        
        if userFounded == False:
            print(ColoredNotification("No Studnt Founded!!!!","red"))
    

    def EditStudent():
        flag = True
        while flag:
            ClearTerminal()
            Managment.UpdateStudentsList()
            print(ColoredNotification("Edit Student", "green"))
            studentId = input("Please Enter the Student ID: ")
            userFounded = False
            for student in Managment.studentsList:
                if student['id'] == int(studentId):
                    print(f"Student ID: {student['id']} | Name: {student['name']} | Age: {student['age']} | Major: {student['major']}")
                    userFounded = True
            if userFounded == False:
                print(ColoredNotification("No Studnt Founded!!!!","red"))
                Wait()
                break
            studentName = input("Please Enter the NEW Student Name: ")
            studentAge = input("Please Enter the NEW Student Age: ")
            studentMajor = input("Please Enter the NEW Student Major: ")
            for index, student in enumerate(Managment.studentsList):
                if student['id'] == int(studentId):
                    selectedStudent = Student(int(studentId), studentName, studentAge, studentMajor)
                    Managment.studentsList[index] = selectedStudent.__dict__
            Managment.UpdateStudentsTxt()
            break


    def DeleteStudent():
        ClearTerminal()
        Managment.UpdateStudentsList()
        print(ColoredNotification("Delete Student", "green"))
        studnetId = input("Please Enter the Student ID: ")
        for index, student in enumerate(Managment.studentsList):
            if student['id'] == int(studnetId):
                Managment.studentsList.pop(index)
        Managment.UpdateStudentsTxt()