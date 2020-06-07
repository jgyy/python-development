# Creating Our First Class
class Car:
    """
    Car models a car w/ tires and an engine
    """

    def __init__(self, engine, tires):
        """
        Car consist of engine and tires
        """
        self.engine = engine
        self.tires = tires

    def description(self):
        """
        Provide description of the car
        """
        print(f"A car with an {self.engine} engine, and {self.tires} tires")

# create a Honda Civic
tires = ['front-driver', 'front-passenger', 'rear-driver', 'rear-passenger']
civic = Car('4-cylinder', tires)
print(civic.tires)
print(civic.engine)
print(civic.description)
print(civic.description())
