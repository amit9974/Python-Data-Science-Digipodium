from audioop import add


def area_of_triangle():
    a = int(input("Enter the length of side A:"))
    b = int(input("Enter the length of side B:"))
    c = int(input("Enter the length of side C:"))
    s = (a + b + c) / 2
    area = (s * (s -a) *(s-b) * (s-c) ** 0.5)
    print("This area of triangle is: ", area)


def area_of_circle():
    r = int(input("Enter the radius of circle: "))
    area = 3.14 * r ** 2
    print("The area of circle is :",area)


def area_of_rectangle():
    l = int(input("Enter the length of rectangle: "))
    w = int(input("Enter the width of rectangle: "))
    area = l + w
    print("The area of the rectangle is", area)


# Main Program is here
def menu():
    print("1. Area of Triangle")
    print("2. Area of circle")
    print("3. Area of Rectangle")
    print("4. Quit")

    choice = input("Enter your choice: ")
    if choice == '1':
        area_of_triangle()
    elif choice == '2':
        area_of_circle()
    elif choice == '3':
        area_of_rectangle()
    elif choice == '4':
        print("GoodBye")
    else:
        print("Invalid Choice")
        menu()

# if __name__ == "__main__":
#     menu()


def add_name(name):
    '''after function name (name) is called parameter'''
    print(f"Hello Mr. {name}")
# add_name('Amit')


def add2_num(x,y):
    c = x + y
    print(c)

# add2_num(2,5)
