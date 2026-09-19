class student:
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks

    def display(self):
        print("Name:",self.name)
        print("Roll No:",self.rollno)
        print("Marks:",self.marks)


if __name__=="__main__":
    s1=student("Alice",101,85)
    s1.display()