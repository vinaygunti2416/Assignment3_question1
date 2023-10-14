class Student:
    

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getRollNumber(self):
        return self.rollNumber

    def setRollNumber(self, rollNumber):
        self.rollNumber = rollNumber

student = Student()
name=input('Enter the name of student: ')
rno=input('Enter the roll no of student: ')
student.setName(name)
student.setRollNumber(rno)

print("Name:", student.getName())
print("Roll Number:", student.getRollNumber())