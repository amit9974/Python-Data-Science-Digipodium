
# Inheritance 

class Person:
    def __init__(self, name, gender='female'):
        self.name = name
        self.gender = gender

    def show(self):
        print("My Details")
        print(f"Name : {self.name}")
        print(f"Gender : {self.gender}")


class Student(Person):
    def __init__(self, name, gender, klass,stream,college):
        super().__init__(name, gender)
        self.klass = klass
        self.college = college
        self.stream = stream

    def show_more_info(self):
        print("More Info ") 
        print(f"Class : {self.klass}") 
        print(f"Stream : {self.stream}")
        print(f"College : {self.college}") 

if __name__ == "__main__":
    p = Person('Amit Kumar', 'Male')
    p.show()

    std = Student('Amit kumar','Male','Python class','Data Science','digipodium')
    std.show()
    std.show_more_info()

class Coder(Student):
    def __init__(self, name, gender, klass, stream, college,prog_lang=[]):
        super().__init__(name, gender, klass, stream, college)
        self.prglang = prog_lang
    
    def coding_experience(self):
        if len(self.prglang) == 0:
            print(f"I {self.name} dont know any programing language")
        else:
            print("I {self.name} know {self.prog_lang} programing language")  
            print("I {self.name} know following programing languages")
            for prog in self.prglang:
                print(f"===> {prog}")
    
    def add_prog_lang(self, lang):
        self.prglang.append(lang)
        print("**"*10)


if __name__=="__main__":
    p = Person('Raj',"Male")
    p.show()
    print("**"*10)

    std1 = Student('Ankit Sharma', "Male","12th","Science","ABC")
    std1.show()
    std1.show_more_info()

    print("**"*10)
    cod = Coder('Rahul','Male','Python','Data Science','Digipodium',['Java'])
    cod.show()
    cod.show_more_info()

    print("**"*10)
    cod.coding_experience()
    print("After 1 Year")
    cod.add_prog_lang('Python')
    cod.add_prog_lang('Java')
    cod.show()
    cod.show_more_info()