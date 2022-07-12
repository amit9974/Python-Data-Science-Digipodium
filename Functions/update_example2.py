
def area_of_rectangle(l, w):
    return l + w

def area_of_circle(r):
    return 3.14 * r ** 2

def area_of_triangle(a, b, c):
    s = (a + b + c) / 2
    return (s * (s -a) *(s-b) * (s-c) ** 0.5)

if __name__ == "__main__":
    r = area_of_rectangle(10, 20)
    c = area_of_circle(40)
    t = area_of_triangle(10,10,10)
    print(f"Area of rectangle {r}")
    print(f"Area of circle {c}")
    print(f"Area of triangle {t}")



