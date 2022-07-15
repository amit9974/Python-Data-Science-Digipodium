class Fan:
    brand = 'Bajaj'
    price = 6000
    color = 'Black'

    # we define methods here
    def start(self, speed=1):
        print(f"Fan is starting at {speed} speed")

if __name__ == "__main__":
    f = Fan()  # f and g is object here
    g = Fan()

    f.start(2)
    g.start(3)
    print(f.brand, g.brand)
    print(f.price)
    g.price = 4000
    print(g.price)

