from dataclasses import dataclass
from pathlib import Path
from typing import List
import csv


@dataclass(frozen=True)
class VehicleHealth:
    timestamp_s: float
    oil_temp_c: float
    battery_v: float
    engine_load_pct: float
    check_engine: bool


def _to_float(value: str, category: str, row: int) -> float:
    try:
        return float(value)
    except ValueError as e:
        raise ValueError(
            f"Row {row}: invalid float for {category}: {value!r}"
        ) from e


def _to_bool(value: str, category: str, row: int) -> bool:
    if value == "1":
        return True
    if value == "0":
        return False
    raise ValueError(
        f"Row {row}: invalid bool for {category}: {value!r}"
    )


def load_vehicle_health(path: Path) -> List[VehicleHealth]:
    # initialize an empty list to store each row from csv
    rows: List[VehicleHealth] = []

    with path.open("r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        # enumerate gives index of each item
        for index, eachRow in enumerate(reader, start=1):
            rows.append(
                VehicleHealth(
                    timestamp_s=_to_float(
                        eachRow["timestamp_s"], "timestamp_s", index),
                    oil_temp_c=_to_float(
                        eachRow["oil_temp_c"], "oil_temp_c", index),
                    battery_v=_to_float(
                        eachRow["battery_v"], "battery_v", index),
                    engine_load_pct=_to_float(
                        eachRow["engine_load_pct"], "engine_load_pct", index),
                    check_engine=_to_bool(
                        eachRow["check_engine"], "check_engine", index)
                    # each element in the dataclass = method (value, category, row(index))
                )
            )
    return rows  # which is a list of vehicleHealth dataclass.
