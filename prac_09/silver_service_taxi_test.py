from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Test some SilverServiceTaxis."""

    # Create SilverServiceTaxi objects with different fanciness values
    hummer_taxi = SilverServiceTaxi("Hummer", 200, 4)
    luxury_taxi = SilverServiceTaxi("Luxury Car", 100, 2)

    # Calculate the fare for an 18 km trip in each SilverServiceTaxi
    distance = 18
    hummer_fare = hummer_taxi.get_fare()
    luxury_fare = luxury_taxi.get_fare()

    # Print the fares
    print(f"{hummer_taxi.name} fare for {distance} km trip: ${hummer_fare:.2f}")
    print(f"{luxury_taxi.name} fare for {distance} km trip: ${luxury_fare:.2f}")


if __name__ == "__main__":
    main()
