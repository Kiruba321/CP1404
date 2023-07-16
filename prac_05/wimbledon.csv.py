DATA_FILENAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2


def main():
    """Read data file, process the data, and display processed information."""
    records = get_records(DATA_FILENAME)
    champion_to_counts, countries = process_records(records)
    display_results(champion_to_counts, countries)


def process_records(records):
    champion_to_count = {}
    countries = set()
    for record in records:
        countries.add(record[INDEX_COUNTRY])
        try:
            champion_to_count[record[INDEX_CHAMPION]] += 1
        except KeyError:
            champion_to_count[record[INDEX_CHAMPION]] = 1
    return champion_to_count, countries


def display_results(champion_to_count, countries):
    print("Wimbledon Champions:")
    for champion, count in champion_to_count.items():
        print(f"{champion} {count}")
    print("\nThese", len(countries), "countries have won Wimbledon:")
    countries_string = ", ".join(sorted(countries))
    print(countries_string)


def get_records(filename):
    records = []
    with open(filename, "r", encoding="utf-8-sig") as file:
        file.readline()
        for line in file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


main()


