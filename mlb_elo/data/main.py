from pybaseball import schedule_and_record, cache

cache.enable()


def main():
    data = schedule_and_record(2023, "OAK")
    return data


if __name__ == "__main__":
    print(main())
