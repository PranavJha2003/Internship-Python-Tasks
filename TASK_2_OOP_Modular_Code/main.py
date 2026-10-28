
from pathlib import Path

from drone_project.data_handler import load_observations
from drone_project.exceptions import DroneProjectError


def main():
    """Run the drone observation program."""
    project_folder = Path(__file__).resolve().parent
    csv_path = project_folder / "observations.csv"

    try:
        observations = load_observations(csv_path)

        print(f"Loaded {len(observations)} drone observations.\n")

        for observation in observations:
            print(observation.to_dict())

    except DroneProjectError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
