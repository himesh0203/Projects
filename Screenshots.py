To use this code:
Install necessary libraries.
Code

    pip install pyautogui Pillow
Save the code: Save the code above as a Python file (e.g., auto_screenshot.py).
Run the script:
Code

    python auto_screenshot.py









import pyautogui
import time
import os
from datetime import datetime

def auto_screenshot_reminder(interval_seconds=60, save_directory="screenshots"):
    """
    Takes screenshots automatically at a specified interval and saves them.

    Args:
        interval_seconds (int): The time interval in seconds between screenshots.
        save_directory (str): The directory where screenshots will be saved.
    """
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)
        print(f"Created directory: {save_directory}")

    print(f"Auto-Screenshot Reminder started. Taking screenshots every {interval_seconds} seconds.")
    print(f"Screenshots will be saved in: {os.path.abspath(save_directory)}")
    print("Press Ctrl+C to stop the program.")

    try:
        while True:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = os.path.join(save_directory, f"screenshot_{timestamp}.png")

            try:
                screenshot = pyautogui.screenshot()
                screenshot.save(filename)
                print(f"Screenshot taken and saved as: {filename}")
            except Exception as e:
                print(f"Error taking screenshot: {e}")

            time.sleep(interval_seconds)

    except KeyboardInterrupt:
        print("\nAuto-Screenshot Reminder stopped by user.")

if __name__ == "__main__":
    # You can customize the interval and save directory here
    screenshot_interval = 30  # Take a screenshot every 30 seconds
    output_folder = "my_auto_screenshots"

    auto_screenshot_reminder(interval_seconds=screenshot_interval, save_directory=output_folder)
