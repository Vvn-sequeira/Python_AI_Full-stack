

class Student: 
    def __init__(self,name,reg):
        self.name =name
        self.reg = reg 
        
    def Marks(self , m1 , m2 , m3 , m4 , m5 , m6):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.m4 = m4
        self.m5 = m5
        self.m6 = m6
        

    def Calculate(self):
        self.total = (self.m1 + self.m2 + self.m3 + self.m4 + self.m6 )
        self.percentage = self.total / 6 
        
        if (self.m1 < 35 or self.m2 < 5 or self.m3 < 35 or self.m4 < 35 or self.m5 < 35 or self.m6 < 35 ): 
            self.Grade = "Fali"
        elif self.percentage >85: 
            self.Grade = "Distinction"
        elif self.percentage > 65: 
            self.Grade = "First Class"
        elif self.percentage > 50 : 
            self.Grade = "Second Class"
        elif self.percentage > 35: 
            self.Grade = "Pass"
        else: 
            self.Grade = "Fail"

    def Display(self):
        
        print("\n___________Student Detiails___________")
        print(f"\nStudent Name : {self.name }")
        print(f"Student RegNo : {self.reg}")
        print(f"\n**************Marks***************")
        print(f"Maths: {self.m1}")
        print(f"English : {self.m2 }")
        print(f"Kannada : {self.m3 }")
        print(f"Hindi : {self.m4 }")
        print(f"Sci : {self.m5 }")
        print(f"Social : {self.m6 }")
        print(f"\nTotal: {self.total}")
        print(f"Percentage : {self.percentage}")
        print(f"Grade : {self.Grade}")
        
        

name = input("Enter the Student Name : ")
reg = int(input("Enter Studennt Reg no : "))

s = Student(name , reg )

m1 , m2 , m3 , m4 , m5 , m6 = map(int , input("Enter 6 subjects marks : ").split())

s.Marks(m1 , m2 , m3 , m4 , m5 , m6 )
s.Calculate() 
s.Display() 