"""
>>> import sys
>>> sys.version > "3.5"
True
"""
import math

# python -m doctest -v .\oop_basic\classes.py
class Car:
    """
    Car models a car w/ tires and an engine

    >>> type(Car)
    <class 'type'>
    """

    def __init__(self, engine, tires):
        """
        Car consist of engine and tires

        >>> car = Car('4-cylinder', ['a', 'b', 'c', 'd'])
        >>> (car.engine, car.tires)
        ('4-cylinder', ['a', 'b', 'c', 'd'])
        """
        self.engine = engine
        self.tires = tires

    def description(self):
        """
        Provide description of the car

        >>> car = Car('4-cylinder', ['a', 'b', 'c', 'd'])
        >>> car.description()
        A car with an 4-cylinder engine, and ['a', 'b', 'c', 'd'] tires
        """
        print(f"A car with an {self.engine} engine, and {self.tires} tires")

    def wheel_circumference(self):
        """
        Provide circumference of the car

        >>> tire = Tire('P', 205, 65, 15)
        >>> tires = [tire, tire, tire, tire]
        >>> honda = Car(tires=tires, engine='4-cylinder')
        >>> honda.wheel_circumference()
        80.1
        """
        if len(self.tires) > 0:
            return self.tires[0].circumference()
        else:
            return 0

class Tire:
    """
    Tire represents a tire that would be used with an automobile.

    >>> type(Tire)
    <class 'type'>
    """

    def __init__(self, tire_type, width, ratio, diameter,
                 brand='', construction='R'):
        """
        Design details of a tire.

        >>> tire = Tire('P', 205, 65, 15)
        >>> (tire.tire_type, tire.width, tire.ratio, tire.diameter, tire.brand, tire.construction)
        ('P', 205, 65, 15, '', 'R')
        """
        self.tire_type = tire_type
        self.width = width
        self.ratio = ratio
        self.diameter = diameter
        self.brand = brand
        self.construction = construction

    def __repr__(self):
        """
        Represent the tire's information in the standard notation present
        on the side of the tire. Example: 'P215/65R15'

        >>> Tire('P', 205, 75, 15)
        P205/75R15
        """
        return (f"{self.tire_type}{self.width}/{self.ratio}"
                + f"{self.construction}{self.diameter}")

    def _side_wall_inches(self):
        """
        Calculate the length of side walls in inches.

        >>> tire = Tire('P', 254, 65, 15)
        >>> tire._side_wall_inches()
        6.5
        """
        return (self.width * (self.ratio / 100)) / 25.4

    def circumference(self):
        """
        The circumference of the tire in inches.

        >>> tire = Tire('P', 205, 65, 15)
        >>> tire.circumference()
        80.1
        """
        side_wall_inches = self._side_wall_inches()
        total_diameter = side_wall_inches * 2 + self.diameter
        return round(total_diameter * math.pi, 1)

class SnowTire(Tire):
    """
    Tire represents a snow tire that would be used with an automobile.

    >>> type(SnowTire)
    <class 'type'>
    """

    def __init__(self, tire_type, width, ratio, diameter, chain_thickness, brand='', construction='R'):
        """
        Design details of a snowtire.

        >>> tire = SnowTire('P', 205, 65, 15, 2)
        >>> (tire.tire_type, tire.width, tire.ratio, tire.diameter, tire.chain_thickness, tire.brand, tire.construction)
        ('P', 205, 65, 15, 2, '', 'R')
        """
        super().__init__(tire_type, width, ratio, diameter, brand, construction)
        self.chain_thickness = chain_thickness

    def __repr__(self):
        """
        Represent the snowtire's information in the standard notation present
        on the side of the tire. Example: 'P215/65R15 (Snow)'

        >>> SnowTire('P', 205, 75, 15, 2)
        P205/75R15 (Snow)
        """
        return super().__repr__() + " (Snow)"

    def circumference(self):
        """
        The circumference of a tire w/ show chains in inches.

        >>> tire = SnowTire('P', 205, 65, 15, 2)
        >>> tire.circumference()
        92.7
        """
        side_wall_inches = self._side_wall_inches()
        total_diameter = (side_wall_inches + self.chain_thickness) * 2 + self.diameter
        return round(total_diameter * math.pi, 1)

# create a Honda Civic
tires = ['front-driver', 'front-passenger', 'rear-driver', 'rear-passenger']
civic = Car('4-cylinder', tires)
print(civic.tires)
print(civic.engine)
print(civic.description)
print(civic.description())

# pass a list of Tire instances as tires when we create a Car
tire = Tire('P', 205, 55, 15)
tires = [tire, tire, tire, tire]
honda = Car(tires=tires, engine='4-cylinder')
honda.description()
print(honda.wheel_circumference())
honda.tires = []
print(honda.wheel_circumference())
