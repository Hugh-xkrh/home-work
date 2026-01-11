from vehicle_health import load_vehicle_health
from pathlib import Path


def main() -> None:
    csv_path = Path(__file__).parent.parent / "data" / "vehicle_health.csv"
    vehicle_health_data = load_vehicle_health(csv_path)

    print(f"Loaded {len(vehicle_health_data)} vehicle health samples")
    print("vehicle health")
    for vh in vehicle_health_data:
        print(vh)


if __name__ == "__main__":
    main()
