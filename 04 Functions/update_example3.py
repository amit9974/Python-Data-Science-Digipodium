
# generate_marks()
def generate_marks(totalmarks):
    if totalmarks >= 90:
        return 'A'
    elif totalmarks >=80:
        return 'B'
    elif totalmarks >= 60:
        return 'C'
    else:
        return 'FAIL'

if __name__ == "__main__":
    grade = generate_marks(55)
    print(f"The grade is {grade}")