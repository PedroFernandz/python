#!/usr/bin/python3

# Import necessary libraries
import RPi.GPIO as GPIO
import time
import os
import signal
import sys

# Set up the fan control pin configuration (GPIO14 = pin 8)
FAN_PIN = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(FAN_PIN, GPIO.OUT)

# Initialize PWM control with a frequency of 25 Hz on the fan pin
pwm = GPIO.PWM(FAN_PIN, 25)
pwm.start(0)

# Function to read the CPU temperature using the 'vcgencmd measure_temp' command
def read_cpu_temperature():
    temp = os.popen("vcgencmd measure_temp").readline()
    temp = temp.replace("temp=", "").replace("'C\n", "")
    return float(temp)

# Function to control the fan speed and save it to a file
def control_fan_speed(speed):
    # Write the fan speed to a file for later reference
    with open("/tmp/fan_speed.txt", "w") as f:
        f.write(str(speed))
    # Change the PWM duty cycle to adjust the fan speed
    pwm.ChangeDutyCycle(speed)

# Function to define a fan operating curve based on the temperature
def fan_speed_curve(temperature):
    if temperature < 55:
        return 0
    elif 55 <= temperature < 65:
        return 25
    elif 65 <= temperature < 72:
        return 50
    elif 72 <= temperature < 77:
        return 75
    else:
        return 100

# Function to handle the shutdown signal and clean up GPIO resources
def shutdown_handler(signum, frame):
    print("\nTerminating the program...")
    pwm.stop()
    GPIO.cleanup()
    sys.exit(0)

# Register the shutdown function as the handler for SIGTERM and SIGINT signals
signal.signal(signal.SIGTERM, shutdown_handler)
signal.signal(signal.SIGINT, shutdown_handler)

try:
    while True:
        # Get the current CPU temperature
        cpu_temperature = read_cpu_temperature()
        print(f"CPU Temperature: {cpu_temperature}°C")

        # Adjust the fan speed according to the operating curve
        control_fan_speed(fan_speed_curve(cpu_temperature))

        # Wait for a while (1 second) before the next temperature reading
        time.sleep(1)

except KeyboardInterrupt:
    shutdown_handler(None, None)
