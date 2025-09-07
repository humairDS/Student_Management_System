class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def student_det(self):
        return {
            "Name": self.name,
            "Roll Number": self.roll_no,
            "Marks": self.marks
        }
