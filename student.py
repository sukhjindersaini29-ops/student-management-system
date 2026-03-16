####################################### STUDENT MANAGEMENT SYSTEM #######################################
# Project Progress Plan
# Step 1 → Create Student class
# Step 2 → Create Student Manager class
# Step 3 → Add student
# Step 4 → Display students
# Step 5 → Search student
# Step 6 → Update student
# Step 7 → Delete student
# Step 8 → Menu driven program
# Step 9 → File saving (optional advanced)

class Student:

    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks

    def to_dict(self):
        return {
            'roll': self.roll,
            'name': self.name,
            'marks': self.marks
        }

    @classmethod
    def from_dict(cls, data): # cls = Student class itself
        return cls(data['roll'], data['name'], data['marks'])