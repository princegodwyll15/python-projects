import csv
import random
from datetime import datetime

def main():
    current_date_and_time = datetime.now()
    PRODUCT_INDEX = 0
    try:
        products = read_dictionary("products.csv", PRODUCT_INDEX)
    except FileNotFoundError:
        print("Product File not found")
        return
    except PermissionError:
        print("Permission denied")
        return

    request_dict = {}
    try:
        with open("request.csv", "rt") as request_file:
            reader = csv.reader(request_file)
            next(reader)
            for each_request in reader:
                if len(each_request) != 0:
                    key = each_request[PRODUCT_INDEX]
                    request_dict[key] = each_request[1:]
    except FileNotFoundError:
        print("Request File not found")
        return
    except PermissionError:
        print("Permission denied")
        return

    print("Godwyll's Shop")
    print("Items:")
    subtotal = 0
    tax = 0
    total = 0
    total_quantities = 0
    for product_num, quantity in request_dict.items():
        try:
            product_info = products[product_num]
        except KeyError:
            print(f"Product {product_num} not found in products dictionary")
            continue
        name_of_product = product_info[0]
        price_of_product = float(product_info[1])
        print(f"{name_of_product}: {quantity[0]} @ ${price_of_product:.2f}")
        #total without sales tax
        subtotal += price_of_product * int(quantity[0])
        #calculating slaes tax
        tax += price_of_product * int(quantity[0]) * 0.06
        #total with sales tax included
        total += price_of_product * int(quantity[0]) * 1.06
        total_quantities += int(quantity[0])
        print()
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Sales Tax: ${tax:.2f}")
    print(f"Total: ${total:.2f}")
    print(f"Total Quantities: {total_quantities}")
    print("Thank you for shopping at the Godwyll's Shop!")
    print()

    # Discount prices by 10% if today is Tuesday or Wednesday
    if datetime.now().weekday() in [1, 2]:
        subtotal *= 0.9
        tax *= 0.9
        total *= 0.9
        print(f"Its {current_date_and_time:%A %I:%M %p} you had a discount of 10% your new total is: ${total} ")

    # Discount prices by 10% if current time is before 11:00 a.m.
    if datetime.now().hour < 11:
        subtotal *= 0.9
        tax *= 0.9
        total *= 0.9
        print(f"Its {current_date_and_time:%A %I:%M %p} you had a discountof 10% your new total is: ${total} ")


    get_coupon_from_product = random.choice(list(request_dict.keys()))
    print(f"Coupon: {get_coupon_from_product} - 10% off next purchase")
    print("Thank you for shopping at the Godwyll's Shop!")
    print("Please complete our online survey to help us improve our services.")
    print()
    print(f"Date: {current_date_and_time:%A %I:%M %p}")


def read_dictionary(filename, key_column_index):
    product_dict = {}
    try:
        with open(filename, "rt") as product_file:
            reader = csv.reader(product_file)
            next(reader)
            for each_product in reader:
                if len(each_product) != 0:
                    key = each_product[key_column_index]
                    product_dict[key] = each_product[1:]
    except FileNotFoundError:
        print("File not found")
        return {}
    except PermissionError:
        print("Permission denied")
        return {}
    return product_dict

if __name__ == "__main__":
    main()


