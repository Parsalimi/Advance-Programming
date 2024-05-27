class AdminManagment:
    
    adminsList = []

    def UpdateStudentsList():
        AdminManagment.adminsList = []
        with open("S12_14020307\\DB\\admin.txt","r") as file:
            for line in file.readlines():
                AdminManagment.adminsList.append(eval(line))

    def Login(username, password):
        AdminManagment.UpdateStudentsList()
        for admin in AdminManagment.adminsList:
            if admin["username"] == username and admin["password"] == password:
                return True
            else:
                return False
