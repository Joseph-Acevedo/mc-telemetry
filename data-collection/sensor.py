from abc import ABC, abstractmethod
from enum import Enum
from typing import Callable
import countio

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

    sensor_type = SensorType.UNKNOWN

    @abstractmethod
    async def initialize(self):
        pass

    @abstractmethod
    def is_initialized(self):
        pass

    def get_sensor_type(self):
        return self.__sensor_type

class GoProSensor(Sensor):

    def __init__(self):
        self.__initialized = False
        self.__sensor_type = SensorType.GOPRO

    async def initialize(self) -> status.Status:
        return status.UnimplementedError("GoPro initialize not implemented.")

    def is_initialized(self) -> bool:
        return self.__initialized

class BrakePressureSensor(Sensor):
    
    def __init__(self):
        self.__initialized = False
        self.__sensor_type = SensorType.BRAKE

    async def initialize(self) -> status.Status:
        return status.UnimplementedError("Brake sensor initialize not implemented.")

    def is_initialized(self) -> bool:
        return self.__initialized

class InputButton(Sensor):

    def __init__(self):
        self.__initialized = False
        self.__sensor_type = SensorType.IO_BUTTON
        self.__callback = None

    async def initialize(self) -> status.Status:
        # Step 1: Initialize the output pin
        # Step 2: Set the color to BUSY
        # Step 3: Initialize the input pin
        return status.UnimplementedError("Button initialize not implemented.")

    def is_initialized(self) -> bool:
        return self.__initialized
    
    def set_trigger_callback(self, callback: Callable):
        self.__callback = callback