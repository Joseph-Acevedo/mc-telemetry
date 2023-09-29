from abc import ABC, abstractmethod
from enum import Enum
from typing import Callable
import RPi.GPIO as GPIO

import status

class SensorType(Enum):
    UNKNOWN = 0
    GOPRO = 1
    BRAKE = 2
    IO_BUTTON = 3

class ColorState(Enum):
    # Actually in-use: BUSY
    OKAY =      (0, 0, 0)
    WARNING =   (0, 0, 0)
    ERROR =     (0, 0, 0)

    BUSY =      (0, 0, 0)
    WAITING =   (0, 0, 0)
    RECORDING = (0, 0, 0)


class Sensor(ABC):

    def __init__(self):
        self.__is_initialized = False
        self.__sensor_type = SensorType.UNKNOWN

    # Performs any necessary hardware setup for the sensor and begins
    # communication.
    @abstractmethod
    async def initialize(self):
        pass

    # Performs any necessary tear down of the Sensor prior to closing
    # the program.
    @abstractmethod
    async def desctruct(self):
        pass

    def is_initialized(self):
        self.__is_initialized

    def get_sensor_type(self):
        return self.__sensor_type

class GoProSensor(Sensor):

    def __init__(self):
        super().__init__()
        self.__sensor_type = SensorType.GOPRO

    async def initialize(self) -> status.Status:
        return status.UnimplementedError("GoPro initialize not implemented.")

    async def destruct(self):
        pass

class BrakePressureSensor(Sensor):
    
    def __init__(self):
        super().__init__()
        self.__sensor_type = SensorType.BRAKE

    async def initialize(self) -> status.Status:
        return status.UnimplementedError("Brake sensor initialize not implemented.")

    async def destruct(self):
        pass

class InputButton(Sensor):

    def __init__(self):
        super().__init__()
        self.__sensor_type = SensorType.IO_BUTTON
        self.__press_counter = 0

    async def initialize(self) -> status.Status:
        GPIO.setmode(GPIO.BCM)
        # Step 1: Initialize the output pin.
        # TODO: Add config reading for output pin.
        GPIO.setup(17, GPIO.OUT, pull_up_down=GPIO.PUD_UP)
        # Step 2: Set the color to BUSY
        self.set_output_color(ColorState.BUSY)
        # Step 3: Initialize the input pin
        # TODO: Add config reading for input pin.
        GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(18, GPIO.FALLING, callback=self.__button_press_callback, bouncetime=100)
        return status.UnimplementedError("Button initialize not implemented.")

    async def destruct(self):
        GPIO.cleanup()

    def set_output_color(self, color: ColorState):
        return
    
    # Returns True if the button has been pressed more than once since the
    # last time a press was received. If True, resets the press counter.
    def was_pressed(self) -> bool:
        if self.__press_counter > 0:
            self.__press_counter = 0
            return True
        return False
    
    # Internal callback for receiving button press interrupts.
    def __button_press_callback(self):
        self.__press_counter += 1