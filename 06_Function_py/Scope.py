
# def name():
#     Name = "vivian"
#     print(Name)

# name()
# Name = "Marcle"
# print(Name)


def chai_order():
    chai = "Vanila chai"

    def print_order():
        chai = "choco chai"
        print(f"Inner fun : {chai}")
    print_order()
    print(f"Outer Fun : {chai}")

chai_order()    
chai = "Ginger"
print(f"Global fun : {chai}")

