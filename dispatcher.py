from driver import Driver
from rider import Rider, WAITING
from location import Location


class Dispatcher:
    """A dispatcher fulfills requests from riders and drivers for a
    ride-sharing service.

    When a rider requests a driver, the dispatcher assigns a driver to the
    rider. If no driver is available, the rider is placed on a waiting
    list for the next available driver. A rider that has not yet been
    picked up by a driver may cancel their request.

    When a driver requests a rider, the dispatcher assigns a rider from
    the waiting list to the driver. If there is no rider on the waiting list
    the dispatcher does nothing. Once a driver requests a rider, the driver
    is registered with the dispatcher, and will be used to fulfill future
    rider requests.
    """

    def __init__(self):
        """Initialize a Dispatcher.

        @type self: Dispatcher
        @rtype: None
        """
        self.wait_list = []
        self.drivers = []

    def __str__(self):
        """Return a string representation.

        @type self: Dispatcher
        @rtype: str

        >>> dispatcher1 = Dispatcher()
        >>> str(dispatcher1)
        Dispatcher
        Riders Waiting: []
        Drivers Waiting: []
        """
        return "Dispatcher \nRiders Waiting: {} \nDrivers Waiting: {}".format(self.wait_list, self.drivers)

    def request_driver(self, rider):
        """Return a driver for the rider, or None if no driver is available.

        Add the rider to the waiting list if there is no available driver.

        @type self: Dispatcher
        @type rider: Rider
        @rtype: Driver | None

        >>> dispatcher1 = Dispatcher()
        >>> driver1 = Driver("Bob", Location(2 ,3), 1)
        >>> rider1 = Rider("Jim", Location(1, 1), Location(2, 3),\
            "waiting", 1)
        >>> dispatcher1.request_rider(driver1)
        >>> print(dispatcher1.request_driver(rider1))
        Bob
        """
        driver = None
        if len(self.drivers) == 0:
            rider.status = WAITING
            self.wait_list.append(rider)
            return None
        else:
            for i in range(len(self.drivers)):
                if driver is None and self.drivers[i].is_idle:
                    driver = self.drivers[i]
                elif (driver is not None and self.drivers[i].is_idle and
                        (self.drivers[i].get_travel_time(rider.origin) < driver.get_travel_time(rider.origin))):
                    driver = self.drivers[i]
        return driver

    def request_rider(self, driver):
        """Return a rider for the driver, or None if no rider is available.

        If this is a new driver, register the driver for future rider requests.

        @type self: Dispatcher
        @type driver: Driver
        @rtype: Rider | None

        >>> dispatcher1 = Dispatcher()
        >>> driver1 = Driver("Sally", Location(2 ,3), 1)
        >>> rider1 = Rider("Billy", Location(1, 1), Location(2, 3),\
            "waiting", 1)
        >>> dispatcher1.request_driver(rider1)
        >>> print(dispatcher1.request_rider(driver1))
        Billy
        """
        rider = None
        found = False
        if driver not in self.drivers:
            self.drivers.append(driver)
        if len(self.wait_list) != 0:
            for i in range(len(self.wait_list)):
                if self.wait_list[i].status == WAITING and not found:
                    rider = self.wait_list[i]
                    found = True
        return rider

    def cancel_ride(self, rider):
        """Cancel the ride for rider.

        @type self: Dispatcher
        @type rider: Rider
        @rtype: None
        """
        index = 0
        found = False
        while index < len(self.wait_list) and not found:
            if self.wait_list[index].id == rider.id:
                found = True
            else:
                index += 1
        if found:
            del self.wait_list[index]
