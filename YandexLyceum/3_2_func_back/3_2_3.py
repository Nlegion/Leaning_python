def average(values: list) -> float:
    lenval = len(values)
    if lenval == 0:
        return 0.0
    return sum(values) / lenval