from enum import Enum

class StatusCode(Enum):
    OKAY = 1
    ERROR = 2
    UNIMPLEMENTED = 3
    UNINITIALIZED = 4

class Status:
    def __init__(self, status: StatusCode, message: str="Okay."):
        self.__status = status
        self.__message = message
    
    def is_okay(self):
        return self.__status == StatusCode.OKAY

    def get_message(self):
        return self.__message
    
def OkayStatus():
    return Status(StatusCode.OKAY)

def UnimplementedError(message: str):
    return Status(StatusCode.UNIMPLEMENTED, message)

def UninitializedError(message: str):
    return Status(StatusCode.UNINITIALIZED, message)

def CollapseStatuses(statuses: list) -> Status:
    failure_message = "".join([f"\t-{status.get_message()}.\n" for status in statuses if not status.is_okay()])
    if len(failure_message) == 0:
        return OkayStatus()
    return UninitializedError(f"Failed to initialize sensors. Errors:\n{failure_message}")
    
    