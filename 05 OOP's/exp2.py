# Constructor is allow to set the property
class Paratha:
    def __init__(self, typ, price):
        self.typ = typ #object variable
        self.price = price
    
    def display(self):
        print(f'{self.typ} : {self.price}')

if __name__ == "__main__":
    ap = Paratha("Aloo Paratha", 30)
    ab = Paratha("Paneer Paratha",50)
    ac = Paratha("Pyaaz Paratha", 40)
    ad = Paratha("Egg Paratha", 30)

    print("Today's Menu")
    ap.display()
    ab.display()
    ac.display()
    ad.display() 

class Employee:
    def __init__(self, name, age, company, salary):
        self.name = name
        self.age = age
        self.company = company
        self.salary = salary

    def show_emp_details(self):
        print(f"Hi Mr.{self.name}\nYour age is {self.age}\nYour company is {self.company}\nYour salary is {self.salary}")

if __name__ == "__main__":
    name = Employee("Amit Kumar",23,"HCL",30000)
    name.show_emp_details()
