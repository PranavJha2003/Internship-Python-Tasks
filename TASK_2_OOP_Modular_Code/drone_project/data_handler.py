
import csv

from .exceptions import InvalidObservationError
from .observation import DroneObservation
from .sensors import TemperatureSensor, HumiditySensor


def load_observations(csv_path):
    """Read drone observations from a CSV file."""
    observations = []

    try:
        with open(csv_path, "r", newline="", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)

            required_columns = {"drone_id", "location", "temperature"}

            if not reader.fieldnames or not required_columns.issubset(
                set(reader.fieldnames)
            ):
                raise InvalidObservationError(
                    "CSV must contain drone_id, location, and temperature columns."
                )

            for row in reader:
                drone_id = (row.get("drone_id") or "").strip()
                location = (row.get("location") or "").strip()
                temperature_text = (row.get("temperature") or "").strip()

                if not drone_id or not location:
                    raise InvalidObservationError(
                        "Drone ID and location cannot be empty."
                    )

                observation = DroneObservation(drone_id, location)

                if temperature_text:
                    try:
                        temperature = float(temperature_text)
                    except ValueError as exc:
                        raise InvalidObservationError(
                            f"Invalid temperature for {drone_id}."
                        ) from exc

                    observation.add_sensor(
                        TemperatureSensor(f"{drone_id}-TEMP", temperature)
                    )

                humidity_text = (row.get("humidity") or "").strip()

                if humidity_text:
                    try:
                        humidity = float(humidity_text)
                    except ValueError as exc:
                        raise InvalidObservationError(
                            f"Invalid humidity for {drone_id}."
                        ) from exc

                    observation.add_sensor(
                        HumiditySensor(f"{drone_id}-HUM", humidity)
                    )

                observations.append(observation)

    except OSError as exc:
        raise InvalidObservationError(
            f"Could not read CSV file: {csv_path}"
        ) from exc

    return observations
