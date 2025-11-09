class SmartParkingSystem:
    def __init__(self, total_slots):
        self.total_slots = total_slots
        self.parking_slots = {}  # Dictionary to store slot status: {slot_number: occupied_by_vehicle_id}

        # Initialize all slots as empty
        for i in range(1, total_slots + 1):
            self.parking_slots[i] = None

    def display_status(self):
        print("\n--- Parking Lot Status ---")
        free_slots = 0
        for slot_number, vehicle_id in self.parking_slots.items():
            if vehicle_id is None:
                print(f"Slot {slot_number}: FREE")
                free_slots += 1
            else:
                print(f"Slot {slot_number}: OCCUPIED by {vehicle_id}")
        print(f"Total Free Slots: {free_slots}/{self.total_slots}")
        print("--------------------------")

    def park_car(self, vehicle_id):
        for slot_number, occupant in self.parking_slots.items():
            if occupant is None:
                self.parking_slots[slot_number] = vehicle_id
                print(f"Vehicle {vehicle_id} parked in Slot {slot_number}.")
                return True
        print(f"Parking lot is full. Cannot park Vehicle {vehicle_id}.")
        return False

    def vacate_slot(self, slot_number):
        if 1 <= slot_number <= self.total_slots:
            if self.parking_slots[slot_number] is not None:
                vehicle_id = self.parking_slots[slot_number]
                self.parking_slots[slot_number] = None
                print(f"Slot {slot_number} vacated by Vehicle {vehicle_id}.")
                return True
            else:
                print(f"Slot {slot_number} is already free.")
                return False
        else:
            print("Invalid slot number.")
            return False

# Example Usage
if __name__ == "__main__":
    parking_lot = SmartParkingSystem(total_slots=5)

    parking_lot.display_status()

    parking_lot.park_car("CAR123")
    parking_lot.park_car("BIKE456")
    parking_lot.park_car("TRUCK789")

    parking_lot.display_status()

    parking_lot.vacate_slot(2)
    parking_lot.park_car("VAN007")

    parking_lot.display_status()

    parking_lot.park_car("BUS111") # Attempt to park when full
    parking_lot.park_car("CARXYZ") # Attempt to park when full

    parking_lot.vacate_slot(1)
    parking_lot.park_car("CARXYZ")

    parking_lot.display_status()
