
class DroneProjectError(Exception):
    """Base exception for the drone observation project."""


class InvalidSensorDataError(DroneProjectError):
    """Raised when sensor data is invalid."""


class InvalidObservationError(DroneProjectError):
    """Raised when drone observation data is invalid."""
