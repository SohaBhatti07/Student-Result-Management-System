class Person:
    def __init__(self, name):
        self.name = name



class Student(Person):
    def __init__(self, name):
        super().__init__(name)
        self.marks = 0

    def view_result(self):
        print("\nStudent Name:", self.name)
        print("Marks:", self.marks)



class Teacher(Person):
    def assign_marks(self, student, marks):
        student.marks = marks

        print(self.name, "assigned", marks,
              "marks to", student.name)

        
        file = open("results.txt", "a")
        file.write(student.name + " = " +
                   str(marks) + " marks\n")
        file.close()



student1 = Student("Ali")
teacher1 = Teacher("Sir Ahmed")


teacher1.assign_marks(student1, 85)


student1.view_result()

print("\nResult saved in results.txt file")