import time
import random

while True:
    temperature = round(random.uniform(60.0, 90.0), 2)
    pressure = round(random.uniform(1.0, 5.0), 2)
    status = random.choice(["RUNNING", "STOPPED"])

    print(f"Temperature : {temperature} °C")
    print(f"Pressure    : {pressure} bar")
    print(f"Status      : {status}")
    print("---")

    time.sleep(2)