from pathlib import Path
from vehicle_health import load_vehicle_health


def main() -> None:
    csv_path = Path(__file__).parent.parent / "data" / "vehicle_health.csv"
    vehicle_health = load_vehicle_health(csv_path)

    print(f"Total {len(vehicle_health)} has been read")
    print("All data: ")
    for eachrow in vehicle_health:
        print(eachrow)


if __name__ == "__main__":
    main()
