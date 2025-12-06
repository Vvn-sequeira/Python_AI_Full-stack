import time
import sys
IsFailed = False
marksArray = None
dataSet = None
gradeList = {
        'A': 85,
        'B': 75,
        'C': 65,
        'D': 55,
    }
def Intro():
    print("************** Welcome to the Marks Manager Portal *************************** \n")
    return

def CollectMarks():
    M1 = int(input("Enter your Maths Marks : "))
    M2 = int(input("Enter your Science Marks : "))
    M3 = int(input("Enter your Social Marks : "))
    M4 = int(input("Enter your English Marks : "))
    M5 = int(input("Enter your Kannada Marks : "))
    M6 = int(input("Enter your Computer Sci Marks : "))

    return [M1, M2, M3, M4, M5, M6]

def Calculate(Marks):
    global IsFailed

    Total = 0
    Percentage = 0.0
    
    for element in Marks:
        Total = Total + element

    Percentage = (Total * 100) / 600

    Grade = None
    
    for e in Marks:
        if e < 36:
            Grade = "FAIL"
            global IsFailed
            IsFailed = True

    if Grade is None:
        if Percentage > 85:
            Grade = "Distinction"
        elif Percentage > 75:
            Grade = "First Class"
        elif Percentage > 55:
            Grade = "Second Class"
        elif Percentage >= 35:
            Grade = "Just PASS"
        elif Percentage < 35:
            Grade = "FAIL"
            IsFailed = True

    data = {
        "total": Total,
        "Percent": Percentage,
        "grade": Grade
    }
    return data

def DisplayData(data):
    print("\n--------------------Marks Display------------------------")
    print("the Total marks of Student is : ", data["total"])
    print("the  Perecentage of Student is : ", data["Percent"],"%")
    print("the  Grade of Student is : ", data["grade"])


def Suggestion(marksArray):
    # check the subject name that sudent has failed ...
    print("\n---------------------------Failed Subject-----------------------------")
    labels = {
        "1" : "Maths",
        "2" : "Science",
        "3" : "Social",
        "4" : "English",
        "5" : "Kannada",
        "6" : "Computer Sci",
    }
    for idx,i in enumerate(marksArray , start=1):
        if i < 35 :
            print(f"Student has failed in {labels[str(idx)]} subject by scoring {i}/100 ")

def CalculateForFuture():
    global dataSet
    global gradeList
    
    tuple_array = tuple(gradeList.items())
    print("-------------------------------------------------------------------")
    print(f"You'r current Grade is {dataSet['grade']}")
    wishGrade = input("What grade are you expecting for next year? ").strip().upper()

    for i , j in tuple_array:
        if i == wishGrade:
            required_Value = j - int(dataSet['Percent'])
            break;
    if required_Value < 1:
        print("Can't calculate the Grade below than the current Grade!")
    else:
        print(f"User required {required_Value}% more to get the desired Grade .... ")

def Options():
    global marksArray
    while(True):
      print(f"\n Options : \n 1. Get to know how much to score to get good Percentage in next Semester exam \n 2.List of Failed Subject \n 3. Exit ")
      reply = int(input())
      if reply == 1:
        CalculateForFuture()
      elif reply == 2:
         if IsFailed : 
           Suggestion(marksArray)
         else:
            print("Student has Passed all the exam.")
            break
      elif reply == 3:
          sys.exit("Exiting!!")

      time.sleep(0.5)


def MarksManagerPortal():
    global marksArray
    global dataSet
    Intro()
    marksArray = CollectMarks()
    dataSet = Calculate(marksArray)
    DisplayData(dataSet)
    Options()


MarksManagerPortal()