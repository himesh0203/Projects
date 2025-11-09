class ParkingSystem:
    def __init__(self, big_slots: int, medium_slots: int, small_slots: int):
        """
        Initializes the parking system with the given number of slots for each car type.
        :param big_slots: Number of available slots for big cars.
        :param medium_slots: Number of available slots for medium cars.
        :param small_slots: Number of available slots for small cars.
        """
        self.slots = {
            1: big_slots,    # CarType 1: Big
            2: medium_slots, # CarType 2: Medium
            3: small_slots   # CarType 3: Small
        }

    def addCar(self, car_type: int) -> bool:
        """
        Attempts to park a car of a specific type.
        :param car_type: The type of car attempting to park (1: big, 2: medium, 3: small).
        :return: True if the car is successfully parked, False otherwise.
        """
        if car_type not in self.slots:
            print(f"Invalid car type: {car_type}")
            return False

        if self.slots[car_type] > 0:
            self.slots[car_type] -= 1
            print(f"Car of type {car_type} parked successfully. Remaining slots: {self.slots[car_type]}")
            return True
        else:
            print(f"No available slots for car type {car_type}.")
            return False

    def get_available_slots(self) -> dict:
        """
        Returns the current number of available slots for each car type.
        :return: A dictionary showing available slots.
        """
        return self.slots

# Example Usage:
if __name__ == "__main__":
    parking_lot = ParkingSystem(big_slots=1, medium_slots=1, small_slots=0)

    print("Initial available slots:", parking_lot.get_available_slots())

    # Attempt to park cars
    parking_lot.addCar(1) # Park a big car
    parking_lot.addCar(2) # Park a medium car
    parking_lot.addCar(3) # Attempt to park a small car (no slots)
    parking_lot.addCar(1) # Attempt to park another big car (no slots left)

    print("Final available slots:", parking_lot.get_available_slots())
