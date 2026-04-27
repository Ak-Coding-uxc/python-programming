"""Example usage for the weight converter."""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.weight_converter import convert_weight

EXAMPLE_WEIGHT = 70.0
EXAMPLE_UNIT = "k"


converted_weight, converted_unit = convert_weight(EXAMPLE_WEIGHT, EXAMPLE_UNIT)
print(f"{EXAMPLE_WEIGHT} {EXAMPLE_UNIT} = {round(converted_weight, 3)} {converted_unit}")
