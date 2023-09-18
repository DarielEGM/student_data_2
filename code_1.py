class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def info_person(self):
        print(f"The person's name is {self.name} and their age is {self.age}")
        
            
class Student(Person):
    def __init__(self, name, age, school_grade):
        super().__init__(name, age)
        self.school_grade = school_grade

    def school_grade_person(self):
        print(f"The person's school grade is {self.school_grade}")
        

Name = input("Whats is your name?: ")
Age = input("How old are you?: ")
School_grade = input("Whats is your school grade?: ")

student = Student(Name, Age, School_grade)

student.info_person()
student.school_grade_person()