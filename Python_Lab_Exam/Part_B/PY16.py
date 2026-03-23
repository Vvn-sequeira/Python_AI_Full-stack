class LowIncomeError(Exception):
    pass 

class Bank:
    count = 0 
    def __init__(self, n , id):
        self.name = n
        self.cust_id = id 
        self.count += 1 
        
class Loan(Bank):
    bank_fund = 50000 
    sanctioned_amt = 0 
    loan_amt = 0 
    
    def __init__(self, name , cid , income ):
        super().__init__(name , cid)
        self.income = income
        
    def grantLoan(self , amt):
        try: 
            if self.income < 20000:
                raise LowIncomeError
            if self.bank_fund - self.sanctioned_amt < amt: 
                raise ValueError
            self.loan_amt = amt 
            print("Loan granted Successfully ")
        except LowIncomeError:
            print("Low income !")
        except ValueError:
            print("bank has Low Fund right NOW ")


    def display(self):
        print(f"Custommer Name : {self.name}")
        print(f"Custommer CID : {self.cust_id}")
        print(f"Custommer Loan Sanctioned : {self.loan_amt}")
        
    
    
choice = "Y"
cust_list = list() 

while choice == "Y": 
    name = input("Enter the Cust name : ")
    id = int(input("Enter the cust id : "))
    loan = int(input("Entet the loan to req "))
    Income = int(input("Entet Your Income ! "))
    cust = Loan(name , id , Income)
    cust.grantLoan(loan)
    cust_list.append(cust)
    choice = input("Do you want to continue Y/N")

    
print("\n \t Customer Details : ")
for i in cust_list:
    i.display()
    print()
        