class Car:
    def __init__(self, model='', year=0):
        self.model = model
        self.year = year
        self.speed = 0
    
    def saveCar(self, model, year):
        self.model = model
        self.year = year
    def increseSpeed(self, accelerate):
        if(accelerate>0):
            print(f'speed increased by {accelerate}')
        else:
            print(f'Invalid input')
        self.speed = accelerate


car = Car()
print(car.saveCar('Toyota',2003))
car.increseSpeed(23)
print(car.speed)
print(car.model)

