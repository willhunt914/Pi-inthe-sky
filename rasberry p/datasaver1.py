##credit for code goes to afton
import board
import busio
import adafruit_mpu6050
import digitalio
from time import sleep, monotonic

led = digitalio.DigitalInOut(board.GP3)
led.direction = digitalio.Direction.OUTPUT
sled = digitalio.DigitalInOut(board.LED)
sled.direction = digitalio.Direction.OUTPUT
sda_pin = board.GP16
scl_pin = board.GP17
i2c = busio.I2C(scl_pin, sda_pin)
imu = adafruit_mpu6050.MPU6050(i2c,address = 0x68)
 
delay = .15
print(monotonic())
with open("/data.csv", "a") as datalog: # Opens / creates a file called data.csv to which the data is stored to
    while True:
        print(f"Accel: {round(imu.acceleration[0]-.6,1)}, {round(imu.acceleration[1]+.2,1)}, {round(imu.acceleration[2],1)}") # Prints the acceleration
        if abs(imu.acceleration[0]-.6) > 9.3 or abs(imu.acceleration[1]+.2) > 9.3:
            led.value = True
            tilt = 1
        else:
            led.value = False
            tilt = 0

        datalog.write(f"{monotonic()},{imu.acceleration[0]},{imu.acceleration[1]},{imu.acceleration[2]},{tilt}\n") # Writes the time, x, y, z acceleration, and if tilted to a file 
        datalog.flush()

        sled.value = True # Flashes onboard LED
        sleep(delay/2)
        sled.value = False
        sleep(delay/2)
