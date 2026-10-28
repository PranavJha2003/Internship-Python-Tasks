
from .exceptions import InvalidSensorDataError


class SensorData:
    """Base class for sensor readings."""

    def __init__(self, sensor_id, value, unit):
        if not sensor_id or not sensor_id.strip():
            raise InvalidSensorDataError("Sensor ID cannot be empty.")

        if value is None:
            raise InvalidSensorDataError("Sensor value cannot be None.")

        self.sensor_id = sensor_id.strip()
        self.value = value
        self.unit = unit

    def get_reading(self):
        return {
            "sensor_id": self.sensor_id,
            "value": self.value,
            "unit": self.unit,
        }


class TemperatureSensor(SensorData):
    """Sensor that records temperature in Celsius."""

    def __init__(self, sensor_id, value):
        super().__init__(sensor_id, value, "C")


class HumiditySensor(SensorData):
    """Sensor that records relative humidity."""

    def __init__(self, sensor_id, value):
        if not isinstance(value, (int, float)) or not 0 <= value <= 100:
            raise InvalidSensorDataError(
                "Humidity must be a number between 0 and 100."
            )

        super().__init__(sensor_id, value, "%")
