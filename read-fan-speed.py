#It is necessary to be running the fan_speed_control.py script.

#!/usr/bin/python3

# Function to read the fan speed from the /tmp/fan_speed.txt file
def read_fan_speed():
    try:
        with open("/tmp/fan_speed.txt", "r") as f:
            fan_speed = int(f.read())
    except FileNotFoundError:
        fan_speed = None
    return fan_speed

# Read the fan speed percentage from the file
fan_speed_percentage = read_fan_speed()

# Print the fan speed if available, otherwise print an error message
if fan_speed_percentage is not None:
    print(f"Fan speed: {fan_speed_percentage}%")
else:
    print("Could not read the fan speed.")

