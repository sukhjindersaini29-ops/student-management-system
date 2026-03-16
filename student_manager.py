import json
from student import Student

class StudentManager:

    def __init__(self):
        self.students = [] # Stores all student objects.
        self.load_students() # Load students from file when the manager is initialized.
        
    def add_student(self, roll, name, marks):
        student = Student(roll, name, marks)
        self.students.append(student)
        self.save_students() # Save students to file after adding a new student.
        print(f"Student {name} added successfully.")

    def display_students(self):
        if len(self.students) == 0:
            print("No students to display.")
            return

        for s in self.students:
            print(f"Roll: {s.roll}, Name: {s.name}, Marks: {s.marks}")
    
    def search_student(self, roll):
        for s in self.students:
            if s.roll == roll:
                print(f"Student found: Roll: {s.roll}, Name: {s.name}, Marks: {s.marks}")
                return
        print("Student not found.")

    def update_student(self, roll):
        for s in self.students:
            if s.roll == roll:
                s.name = input("Enter new name: ")
                s.marks = int(input("Enter new marks: "))
                print("Student updated successfully.")
                self.save_students() # Save students to file after updating a student.
                return
        print("Student not found.")

    def delete_student(self, roll):
        for s in self.students:
            if s.roll == roll:
                self.students.remove(s)
                print("Student deleted successfully.")
                self.save_students() # Save students to file after deleting a student.
                return
        print("Student not found.")
    
    def load_students(self):
        try:
            with open('students.json', 'r') as file:
                data = json.load(file)
                
                for item in data:
                    student = Student.from_dict(item)
                    self.students.append(student)
        except FileNotFoundError:
            pass
    
    def save_students(self):
        data = []

        for s in self.students:
            data.append(s.to_dict())
        
        with open('students.json', 'w') as file:
            json.dump(data, file, indent=4)