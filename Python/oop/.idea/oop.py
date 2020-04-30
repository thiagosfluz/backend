class Kettle(object):

    power_source = "eletricity"


    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def swtich_on(self):
        self.on = True


kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.75
print(kenwood.price)


hamilton = Kettle("Hamilton", 14.55)

print("Models: {}={}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))

print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood,hamilton))

print(hamilton.on)
hamilton.swtich_on()
print(hamilton.on)

Kettle.swtich_on(kenwood)
print(kenwood.on)

kenwood.swtich_on()

print("*" * 80)

kenwood.power = 1.5
print(kenwood.power)

print("Switch to atomic power")
Kettle.power_source = "atomic"

print(Kettle.power_source)
print("Switch Kenwood to gas")
kenwood.power_source = "gas"
print(kenwood.power_source)
print(hamilton.power_source)


print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)