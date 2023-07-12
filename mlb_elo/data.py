from pybaseball import schedule_and_record, cache # type: ignore
from typing import Tuple

cache.enable()

def get_teams() -> Tuple[str, ...]:
    return (
        "ANA", # Anaheim Angels
        "ARI", # Diamondbacks
        "ATL", # Braves
        "BAL", # Orioles
        "BOX", # Red Sox
        "CHC", # Cubs
        "CHW", # White Sox
    )

def main():
    data = schedule_and_record(2023, "OAK")
    return data


if __name__ == "__main__":
    print(main())
