
from dataclasses import dataclass
from pathlib import Path
from typing import List
import csv


@dataclass(frozen=True)
class Vehicle_Health:
    timestamp_s: float
    oil_temp_c: float
    battery_v: float
    engine_load_pct: float
    check_engine: bool


def _to_float(value: str, field: str, row: int) -> float:
    try:
        return float(value)
    except ValueError as e:
        raise ValueError(
            f"Row {row}: invalid float for {field}: {value!r}") from e


def _to_bool(value: str, field: str, row: int) -> bool:
    try:
        if value == "1":
            return True
        elif value == "0":
            return False

    except ValueError as e:
        raise ValueError(
            f"Row {row}: invalid bool for {field}: {value!r}") from e


def load_vehicle_health(path: Path) -> List[Vehicle_Health]:

    rows: List[Vehicle_Health] = []

    with path.open("r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        required = {"timestamp_s", "oil_temp_c",
                    "battery_v", "engine_load_pct", "check_engine"}
        if reader.fieldnames is None:
            raise ValueError("CSV has no header row.")
        missing = required - set(reader.fieldnames)
        if missing:
            raise ValueError(
                f"CSV missing required columns: {sorted(missing)}")

        for i, r in enumerate(reader, start=1):
            rows.append(
                Vehicle_Health(
                    timestamp_s=_to_float(r["timestamp_s"], "timestamp_s", i),
                    oil_temp_c=_to_float(r["oil_temp_c"], "oil_temp_c", i),
                    battery_v=_to_float(r["battery_v"], "battery_v", i),
                    engine_load_pct=_to_float(
                        r["engine_load_pct"], "engine_load_pct", i),
                    check_engine=_to_bool(
                        r["check_engine"], "check_engine", i),
                )
            )
        return rows
