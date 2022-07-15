# creation
def si_calc():
    p = float(input("Enter the principle: "))
    r = float(input("Enter the rate of interest: "))
    t = float(input("Enter the time: "))
    si = p * (r * t) / 100
    print(f"Simple Interest is {si}")
# # usage
# si_calc()

def ci_calc():
    p = float(input("Enter the principle: "))
    r = float(input("Enter the rate of interest: "))
    t = float(input("Enter the time: "))
    ci = p * (1 + r / 100) ** t
    print(f"Simple Interest is {ci}")
    
# ci_calc()


# create function
def Employee_Details():
    '''this function help to add employee's details'''
    name = input("Enter the name: ")
    age = int(input("Enter your age: "))
    company_name = input("Enter your company name: ")
    print(f"Your name is {name}\nYour age is {age}\nYour Company Name is {company_name}")
# # use of function
# Employee_Details()

def Student_Details():
    '''this function help to add students details'''
    name = input("Enter the name of Student: ")
    age = int(input("Enter Student age age: "))
    clas = int(input("Enter student class: "))
    school_name = input("Enter your school name: ")
    print(f"Your name is {name}\nYour age is {age}\nStudent is in class{clas}\nYour Company Name is {school_name}")




def Vehical_Info():
    make = input("Vehicle make : ")
    model = input("Vehicle model : ")
    year = int(input("Vehicle year : "))
    print(f"Vehicle Make is{make}\nVehicle Model is {model}\nVehicle Launch Year is {year}")