
import csv
import tempfile
import unittest
from pathlib import Path

from drone_project.exceptions import (
    InvalidObservationError,
    InvalidSensorDataError,
)
from drone_project.sensors import (
    SensorData,
    TemperatureSensor,
    HumiditySensor,
)
from drone_project.observation import DroneObservation
from drone_project.data_handler import load_observations


class TestDroneProject(unittest.TestCase):

    def test_temperature_sensor_inheritance(self):
        sensor = TemperatureSensor("TEMP-01", 24.5)
        self.assertIsInstance(sensor, SensorData)
        self.assertEqual(sensor.get_reading()["value"], 24.5)

    def test_humidity_validation(self):
        with self.assertRaises(InvalidSensorDataError):
            HumiditySensor("HUM-01", 150)

    def test_observation_composition(self):
        observation = DroneObservation("DR-01", "North Field")
        observation.add_sensor(TemperatureSensor("TEMP-01", 24.5))

        result = observation.to_dict()

        self.assertEqual(result["drone_id"], "DR-01")
        self.assertEqual(len(result["sensors"]), 1)

    def test_invalid_drone_id(self):
        with self.assertRaises(InvalidObservationError):
            DroneObservation("", "North Field")

    def test_load_csv_observations(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            csv_path = Path(temp_dir) / "observations.csv"

            with csv_path.open("w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(
                    ["drone_id", "location", "temperature", "humidity"]
                )
                writer.writerow(["DR-01", "North Field", "24.5", "60"])

            observations = load_observations(csv_path)

            self.assertEqual(len(observations), 1)
            self.assertEqual(observations[0].drone_id, "DR-01")
            self.assertEqual(len(observations[0].sensors), 2)


if __name__ == "__main__":
    unittest.main()
