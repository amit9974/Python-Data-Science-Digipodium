from example1 import ci_calc,si_calc, Employee_Details, Student_Details
from example1 import Vehical_Info


choice1 = input("What you want to be calculate? (si/ci)?: ")
if choice1 == 'si':
    si_calc()
elif choice1 == 'ci':
    ci_calc()
else:
    print("Invalid choice!")


choice = input("Which form is want to fill (1.Employee Form / 2.Student Form): ")
if choice == '1':
    Employee_Details()
elif choice == '2':
    Student_Details()
else:
    print("Invalid choice! ")
