class Vehicle:

    def __init__(self, mpg, vin):
        self.mpg = mpg
        self.vin = vin
        self.setReserved(False)
        self.type = None

    def getType(self):
        return self.type

    def getVin(self):
        return self.vin

    def getDescription(self):
        return 'MPG is {} and VIN is {}'.format(self.mpg, self.vin)

    def isReserved(self):
        return self.reserved

    def setReserved(self, reserved):
        self.reserved = reserved

class Car(Vehicle):

    def __init__(self, make_model, mpg, numPassengers, numDoors, vin):
        Vehicle.__init__(self, mpg, vin)
        self.type = 'Car'
        self.make_model = make_model
        self.numPassengers = numPassengers
        self.numDoors = numDoors

    def getDescription(self):
        return '{} model is {}, with {} doors and can carry {} passengers. MPG is {} and VIN is {}' \
        .format(self.type, self.make_model, self.numDoors, self.numPassengers, self.mpg, self.vin)



v = Car('Ford Focus', 30, 5, 5, 123)
print(v.isReserved())
print(v.getDescription())