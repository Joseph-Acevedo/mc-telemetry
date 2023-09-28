#!/usr/bin/env python3
# mc-telemetry/data-collection/main.py

import asyncio

from sensor import GoProSensor, BrakePressureSensor, InputButton
import status

gopro_sensor = None
pressure_sensor = None
input_button = None

async def startup_sensors() -> status.Status:
    gopro_sensor = GoProSensor()
    pressure_sensor = BrakePressureSensor()
    input_button = InputButton()

    async with asyncio.TaskGroup() as tg:
        button_coroutine = tg.create_task(input_button.initialize())
        gopro_coroutine = tg.create_task(gopro_sensor.initialize())
        pressure_coroutine = tg.create_task(pressure_sensor.initialize())
    
    return status.CollapseStatuses([await button_coroutine, await gopro_coroutine, await pressure_coroutine])

async def main():
    # Start up sensors. TODO: Add status returning.
    startup_sensors()
    pass
    

if __name__ == "__main__":
    asyncio.run(main())

