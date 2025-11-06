pip install psutil pywin32


pip install psutil pyobjc

On Linux, make sure you have xdotool installed:
sudo apt install xdotool



# screen_time_philosopher_pro.py
# Tracks your active applications and reflects on your screen habits with philosophical wisdom.

import time
import psutil
import random
import platform
import datetime
import os

try:
    import win32gui
    import win32process
except ImportError:
    win32gui = None

# Define your wisdom
quotes = {
    "short": [
        "Even brief moments in the digital glow can shape your thoughts.",
        "A mindful minute online is worth an hour of distraction.",
        "Screens flicker, but awareness stays still.",
    ],
    "medium": [
        "You wandered through the digital fields — did you find meaning or memes?",
        "The more tabs we open, the further we drift from ourselves.",
        "Balance is the art of knowing when to log off.",
    ],
    "long": [
        "You have communed long with the machine — what have you learned?",
        "In the endless scroll lies a mirror of our restlessness.",
        "To master technology, one must first master the self.",
    ],
}


def get_active_window_name():
    """Get the current active window name depending on the OS."""
    os_name = platform.system()

    if os_name == "Windows" and win32gui:
        try:
            hwnd = win32gui.GetForegroundWindow()
            _, pid = win32process.GetWindowThreadProcessId(hwnd)
            process = psutil.Process(pid)
            return process.name()
        except Exception:
            return "Unknown"
    elif os_name == "Darwin":  # macOS
        try:
            from AppKit import NSWorkspace
            return NSWorkspace.sharedWorkspace().frontmostApplication().localizedName()
        except Exception:
            return "Unknown"
    elif os_name == "Linux":
        try:
            import subprocess
            active_window = subprocess.check_output(
                ["xdotool", "getactivewindow", "getwindowname"]
            ).decode("utf-8").strip()
            return active_window or "Unknown"
        except Exception:
            return "Unknown"
    else:
        return "Unknown"


def reflect_screen_time(seconds):
    """Choose a quote based on screen time."""
    if seconds < 60:
        return random.choice(quotes["short"])
    elif seconds < 300:
        return random.choice(quotes["medium"])
    else:
        return random.choice(quotes["long"])


def track_activity(duration=60):
    """Track active app usage for a period of time (default: 1 minute)."""
    usage_log = {}
    start_time = time.time()
    print("🧘 Tracking your active apps. Press Ctrl+C to stop early.\n")

    try:
        while True:
            active_app = get_active_window_name()
            usage_log[active_app] = usage_log.get(active_app, 0) + 1
            time.sleep(1)

            elapsed = time.time() - start_time
            print(f"\r⏳ Elapsed: {int(elapsed)}s | Active: {active_app[:30]}", end="")

            if elapsed >= duration:
                break
    except KeyboardInterrupt:
        print("\nTracking manually stopped.")
    finally:
        print("\n\n📊 Summary of your session:")
        for app, seconds in sorted(usage_log.items(), key=lambda x: x[1], reverse=True):
            mins = seconds // 60
            print(f" - {app}: {mins}m {seconds % 60}s")

        total = sum(usage_log.values())
        print(f"\nTotal screen time: {total}s")
        print("\nPhilosopher says:")
        print(f"💬 {reflect_screen_time(total)}\n")

        # Save log
        save_log(usage_log)


def save_log(data):
    """Save usage data with timestamp."""
    filename = "screen_time_log.txt"
    with open(filename, "a") as f:
        f.write(f"\nSession on {datetime.datetime.now()}:\n")
        for app, secs in data.items():
            f.write(f"{app}: {secs}s\n")
        f.write("-" * 30 + "\n")
    print(f"🗂️  Log saved to {filename}")


if __name__ == "__main__":
    print("🖥️ Welcome to the Screen Time Philosopher Pro 🌿")
    print("This program will observe your current app usage in real-time.")
    minutes = input("⏱️ How many minutes should I track? (default: 1): ") or "1"
    duration = int(minutes) * 60
    track_activity(duration)
