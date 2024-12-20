import datetime
print('CODE TO CALCULATE DISCOUNT OF ITEMS PURCHASED AT GODWYLL,S BOUTIQUE ON GIVEN DAYS')

# sales tax associated with your purchase
sub_total = float(input('Please input your sub total here. $'))
print()
def calculate_sales_tax():
    sales_tax = 0.06
    sales_tax_accounted = round(sales_tax * sub_total, 2)
    print(f'The sales tax accounted for on the item you purchased is {sales_tax_accounted}')


# total money to be paid after discount is accounted for
def total_after_discount(sub_total):
    sales_tax = 0.06
    discount = sub_total * 0.1
    total = round(sub_total + sales_tax - discount, 2)
    print(f'The total amount to pay with discount and sales tax included is ${total}')


def total_without_discount(sub_total):
    sales_tax = 0.06
    total = sub_total + sales_tax
    print(f'The total amount to pay with sales tax included is ${total}')


# discount associated with your purchase
def discount_calculation(sub_total):
    discount =round (0.1 * sub_total)
    print(f'The discount associated with your purchase is ${discount}')
        

get_day = datetime.datetime.now()
day_of_the_week = get_day.weekday()
actual_day = get_day.strftime('%A')

if day_of_the_week in [1, 0] and sub_total >= 50:
    print(f'Its {actual_day} and you won a prize which is a discount of 10%')
    calculate_sales_tax()
    discount_calculation(sub_total)
    total_after_discount(sub_total)


else:
    calculate_sales_tax()
    total_without_discount(sub_total)
    print('No discount applied. Thanks for working with us!')

