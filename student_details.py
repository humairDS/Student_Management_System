class student:    #class

    def __init__(self,name,roll_no,marks):   #constructor/initializer

        self.name = name   #Instance Attributes     
        self.roll_no = roll_no #Instance Attributes               
        self.marks = marks #Instance Attributes


    def student_det(self):  #Instance Method
        print(f"Name:{self.name} Roll Number:{self.roll_no} Marks:{self.marks}")

student_details = student("umair",23,87)  #Object


student_details.student_det()  #calling method to display details