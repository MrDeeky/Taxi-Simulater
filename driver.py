from location import Location, manhattan_distance
from rider import Rider


class Driver:
    """A driver for a ride-sharing service.

    === Attributes ===
    @type id: str
        A unique identifier for the driver.
    @type location: Location
        The current location of the driver.
    @type is_idle: bool
        A property that is True if the driver is idle and False otherwise.
    """

    def __init__(self, identifier, location, speed):
        """Initialize a Driver.

        @type self: Driver
        @type identifier: str
        @type location: Location
        @type speed: int
        @rtype: None
        """
        self.id = identifier
        self.location = location
        self.speed = speed
        self.is_idle = True
        self.destination = None

    def __str__(self):
        """Return a string representation.

        @type self: Driver
        @rtype: str

        >>> location1 = Location(3, 4)
        >>> driver1 = Driver("Bob", location1, 1)
        >>> str(driver1)
        Bob
        """
        return self.id

    def __eq__(self, other):
        """Return True if self equals other, and false otherwise.

        @type self: Driver
        @rtype: bool

        >>> location1 = Location(3, 4)
        >>> location2 = Location(5 ,6)
        >>> driver1 = Driver("Bob", location1, 1)
        >>> driver2 = Driver("Tom", location1, 1)
        >>> driver3 = Driver("Bob", location2, 1)
        >>> driver1 == driver2
        False
        >>> driver1 == driver3
        True
        """
        return isinstance(other, Driver) and (self.id == other.id) and (self.location == other.location) and \
            (self.speed == other.speed) and (self.is_idle == other.is_idle) and \
            (self.destination == other.destination)

    def get_travel_time(self, destination):
        """Return the time it will take to arrive at the destination,
        rounded to the nearest integer.

        @type self: Driver
        @type destination: Location
        @rtype: int

        >>> location1 = Location(1, 1)
        >>> destination1 = Location(2, 2)
        >>> driver1 = Driver("Bob", location1, 1)
        >>> print(driver1.get_travel_time(destination1))
        2
        """
        return manhattan_distance(self.location, destination)/self.speed

    def start_drive(self, location):
        """Start driving to the location and return the time the drive will take.

        @type self: Driver
        @type location: Location
        @rtype: int

        >>> location1 = Location(1, 1)
        >>> location2 = Location(3, 3)
        >>> driver1 = Driver("Bob", location1, 1)
        >>> print(driver1.start_drive(location2))
        4
        """
        self.is_idle = False
        self.destination = location
        return self.get_travel_time(location)

    def end_drive(self):
        """End the drive and arrive at the destination.

        Precondition: self.destination is not None.

        @type self: Driver
        @rtype: None
        """
        self.location = self.destination
        self.is_idle = True
        self.destination = None

    def start_ride(self, rider):
        """Start a ride and return the time the ride will take.

        @type self: Driver
        @type rider: Rider
        @rtype: int

        >>> location1 = Location(1, 1)
        >>> location2 = Location(2, 4)
        >>> driver1 = Driver("Bob", location1, 1)
        >>> print(driver1.start_drive(location2))
        4
        """
        self.is_idle = False
        self.destination = rider.destination
        return self.get_travel_time(rider.destination)

    def end_ride(self):
        """End the current ride, and arrive at the rider's destination.

        Precondition: The driver has a rider.
        Precondition: self.destination is not None.

        @type self: Driver
        @rtype: None
        """
        self.is_idle = True
        self.location = self.location
        self.destination = None
