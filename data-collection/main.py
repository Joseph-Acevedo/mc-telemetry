#!/usr/bin/env python3
# mc-telemetry/data-collection/main.py

import asyncio
from sensor import GoProSensor, PressureSensor, InputButton

gopro_sensor = None
pressure_sensor = None
input_button = None

async def startup_sensors():
    gopro_sensor = GoProSensor()
    pressure_sensor = PressureSensor()
    input_button = InputButton()

    await asyncio.gather(gopro_sensor.initialize(), \
                        pressure_sensor.initialize(), \
                        input_button.initialize())



async def main():
    # Start up sensors
    

if __name__ == "__main__":
    asyncio.run(main())

