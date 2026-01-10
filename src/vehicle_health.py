
from dataclasses import dataclass


@dataclass(frozen=True)
class VehicleHealth:
    timestamp_s: float
    oil_temp_c: float
    battery_v: float
    engine_load_pct: float
    check_engine: bool


def to_float(value: str, field: str, row: int) -> float:
    try:
        return float(value)
    except ValueError as e:
        raise ValueError(
            f"Row {row}: invalid float for {field}: {value!r}") from e


def to_bool(value: str, field: str, row: int) -> bool:
    try:
        if value == "1":
            return True
        elif value == "0":
            return False
        else:
            raise ValueError(f"Row {row}: invalid bool for {field}: {value!r}")

    except ValueError as e:
        raise ValueError(
            f"Row {row}: invalid bool for {field}: {value!r}") from e


def load_vehicle_health(path: str) -> list[VehicleHealth]:
    import csv

    rows: list[VehicleHealth] = []

    with open(path, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for i, r in enumerate(reader, start=1):
            rows.append(
                VehicleHealth(
                    timestamp_s=to_float(r["timestamp_s"], "timestamp_s", i),
                    oil_temp_c=to_float(r["oil_temp_c"], "oil_temp_c", i),
                    battery_v=to_float(r["battery_v"], "battery_v", i),
                    engine_load_pct=to_float(
                        r["engine_load_pct"], "engine_load_pct", i),
                    check_engine=to_bool(
                        r["check_engine"], "check_engine", i),
                )
            )

    return rows
