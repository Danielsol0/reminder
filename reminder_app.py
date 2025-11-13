import time
from datetime import datetime

# Ask the user for time and message
reminder_time = input("Enter time in HH:MM format (like 14:30): ")
message = input("What should I remind you about? ")

print(f"Reminder set for {reminder_time}. I’ll remind you!")

# Keep checking the time
while True:
    now = datetime.now().strftime("%H:%M")
    if now == reminder_time:
        print(f"\n⏰ Reminder: {message}")
        break
    time.sleep(30)  # Wait 30 seconds before checking again
