def name():
    Name = "vivian"

    def name_again():
        # nonlocal Name 
        Name = "Marcel"  # without ' nonLocal ' variable Name will be here the Local variable 
    name_again()
    print(f"After updating Name : {Name}")

name()


