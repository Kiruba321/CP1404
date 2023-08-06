from prac_09.unreliable_car import UnreliableCar


def main():
    good_car = UnreliableCar("Mostly Good", 100, 90)
    bad_car = UnreliableCar("Dodgy", 100, 9)

    for i in range(1, 12):
        distance_driven_good = good_car.drive(i)
        distance_driven_bad = bad_car.drive(i)
        print(f"Attempting to drive {i} km:")
        print(f"{good_car.name:12} drove {distance_driven_good} km")
        print(f"{bad_car.name:12} drove {distance_driven_bad} km")

    print("\nFinal states of the cars:")
    print(good_car)
    print(bad_car)


if __name__ == "__main__":
    main()
