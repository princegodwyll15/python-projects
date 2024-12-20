import math
import datetime
import random
phone = ''
print('Code to calculate the volume of a tire in LITRES given the width the  \n'
      'aspect ratio and diameter of the tire. with the following parameters\n\n'
      'w = width in millimeters\n'
      'a = aspect ratio\n'
      'd= diameter in inches .\n')

get_day = datetime.datetime.now()
day_of_the_week = get_day.weekday()
actual_day = get_day.strftime('%A')


w = float(input('Please input the width to proceed (unit is in mm). '))
a = float(input('Please input the aspect ratio to proceed. '))
d = float(input('Please input the diameter to proceed (unit is in ich). '))
print()

# code to covert all values of width and diameter to litres
# 1 millimeter = 0.001 litres
w_in_litres = round(w * 0.001, 5)
d_to_litres = round(d * 0.0254, 5)
formula = round((math.pi * w_in_litres ** 2 * a ** 2) + (2.54 * d_to_litres / 10000000000), 3)


# prices of tire
price_of_tires = {3400, 5500, 4050, 2099, 3099}
random_price = random.choice(list(price_of_tires))


def tire_volume():
    print(f'width in litres is {w_in_litres}l')
    print(f"diameter in litres is {d_to_litres}l\n")
    print(f'The volume of the tire is: {formula} litres')
    print(f'The price of the tire with the dimensions you provided is: ${random_price}')
    print()


tire_volume()


buy = input('Do you want to buy the tire with the dimensions you provided is (yes/y or no): ')
if buy.lower() in ['y', 'yes']:
    phone = int(input('Please input your Phone Number: '))
    print('Thanks very much for working with us.')
else:
    print('Alright then see you next time and we hope you buy from us next time!')


with open('volume.txt', 'w') as file:
    file.write(f'Today is {actual_day}, \n'
               f'The width of the tire in mm is {w}mm\n'
               f'The aspect ratio of the tire is {a}\n'
               f'The diameter of the tire in inches is {d}\n'
               f'Converted width in litres is: {w_in_litres}litres\n'
               f'Converted diameter in litres is {d_to_litres}litres\n'
               f'The total volume of the tire in litres is: {formula}litres\n'
               f'The clients phone number is {phone} ')


