
from .exceptions import InvalidObservationError
from .sensors import SensorData


class DroneObservation:
    """Represents one drone observation with multiple sensor readings."""

    def __init__(self, drone_id, location, sensors=None):
        if not drone_id or not drone_id.strip():
            raise InvalidObservationError("Drone ID cannot be empty.")

        if not location or not location.strip():
            raise InvalidObservationError("Location cannot be empty.")

        self.drone_id = drone_id.strip()
        self.location = location.strip()
        self.sensors = []

        if sensors:
            for sensor in sensors:
                self.add_sensor(sensor)

    def add_sensor(self, sensor):
        """Add a sensor reading to this observation."""
        if not isinstance(sensor, SensorData):
            raise InvalidObservationError(
                "Only valid SensorData objects can be added."
            )

        self.sensors.append(sensor)

    def to_dict(self):
        """Convert the observation into a dictionary."""
        return {
            "drone_id": self.drone_id,
            "location": self.location,
            "sensors": [sensor.get_reading() for sensor in self.sensors],
        }
