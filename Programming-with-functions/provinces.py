def main():
    provinces_list = []
    try:
        with open("provinces.txt", "rt") as provinces_file:
            for each_line in provinces_file:
                clean_line = each_line.strip()
                provinces_list.append(clean_line)
        if len(provinces_list) > 1:  # Check if list has at least 2 elements
            provinces_list.pop(0)
            provinces_list.pop(-1)
        # Replace all occurrences of "AB" with "Alberta"
        provinces_list = [province.replace("AB", "Alberta") for province in provinces_list]
        print(provinces_list)
        # Count the number of elements that are "Alberta" and print that number
        alberta_count = provinces_list.count("Alberta")
        print(f"Number of 'Alberta' elements: {alberta_count}")
    except FileNotFoundError:
        print("Error: provinces.txt not found")

if __name__ == "__main__":
    main()

