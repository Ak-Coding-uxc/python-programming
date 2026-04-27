"""Simple weight conversion utility (kilograms <-> pounds)."""


def convert_weight(weight: float, unit: str) -> tuple[float, str]:
    """Convert `weight` based on `unit`.

    Supported units:
    - "k" for kilograms (converted to pounds)
    - "lbs" for pounds (converted to kilograms)
    """
    if unit == "k":
        return weight * 2.205, "lbs"
    if unit == "lbs":
        return weight / 2.205, "k"
    raise ValueError(f"{unit} is not valid")


def main() -> None:
    """Read user input and print converted weight."""
    weight = float(input("Enter your weight: "))
    unit = input("Enter your unit (k/lbs): ")

    try:
        converted_weight, converted_unit = convert_weight(weight, unit)
    except ValueError as error:
        print(error)
        return

    print(f"Your weight is {round(converted_weight, 3)} {converted_unit}")


if __name__ == "__main__":
    main()
