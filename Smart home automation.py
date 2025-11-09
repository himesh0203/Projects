import time

class SmartDevice:
    """Represents a generic smart home device."""
    def __init__(self, name, device_type):
        self.name = name
        self.device_type = device_type
        self.status = "off" # Default status

    def turn_on(self):
        self.status = "on"
        print(f"{self.name} ({self.device_type}) is now ON.")

    def turn_off(self):
        self.status = "off"
        print(f"{self.name} ({self.device_type}) is now OFF.")

    def get_status(self):
        return self.status

class HomeAutomationSystem:
    """Manages smart devices and automation rules."""
    def __init__(self):
        self.devices = {} # Stores SmartDevice objects

    def add_device(self, device):
        self.devices[device.name] = device

    def control_device(self, device_name, action):
        if device_name in self.devices:
            device = self.devices[device_name]
            if action == "on":
                device.turn_on()
            elif action == "off":
                device.turn_off()
            else:
                print(f"Invalid action for {device_name}.")
        else:
            print(f"Device '{device_name}' not found.")

    def apply_rule(self, rule_name, condition_func, action_func):
        """Applies an automation rule."""
        if condition_func():
            print(f"Rule '{rule_name}' triggered. Executing action...")
            action_func()
        else:
            print(f"Rule '{rule_name}' condition not met.")

# --- Example Usage ---
if __name__ == "__main__":
    automation_system = HomeAutomationSystem()

    # Create devices
    living_room_light = SmartDevice("Living Room Light", "light")
    thermostat = SmartDevice("Thermostat", "climate")
    door_sensor = SmartDevice("Front Door Sensor", "sensor")

    # Add devices to the system
    automation_system.add_device(living_room_light)
    automation_system.add_device(thermostat)
    automation_system.add_device(door_sensor)

    # Manual control
    automation_system.control_device("Living Room Light", "on")
    automation_system.control_device("Thermostat", "on")
    time.sleep(1) # Simulate some time passing

    # Define automation rules
    def night_time_condition():
        # In a real system, this would check time of day, e.g., using datetime module
        current_hour = time.localtime().tm_hour
        return 20 <= current_hour <= 23 # Between 8 PM and 11 PM

    def turn_on_night_light_action():
        automation_system.control_device("Living Room Light", "on")

    def door_open_alert_condition():
        # Simulate a sensor reading (e.g., from a physical sensor)
        # For this example, we'll just assume it's "open" for demonstration
        return True # Replace with actual sensor reading

    def send_notification_action():
        print("ALERT: Front door is open!")

    # Apply rules
    print("\nApplying automation rules:")
    automation_system.apply_rule("Night Light", night_time_condition, turn_on_night_light_action)
    automation_system.apply_rule("Door Open Alert", door_open_alert_condition, send_notification_action)

    time.sleep(1)
    automation_system.control_device("Living Room Light", "off")
    automation_system.control_device("Thermostat", "off")
