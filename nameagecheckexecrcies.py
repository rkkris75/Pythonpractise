# name = input("Please enter your name")
# age = int(input('Please enter your age {}'.format(name)))
#
# if 18 < age < 31:
#     print("Welcome to holiday!!!")
# else:
#     print("Mr.{}, Please be advised that you are not in a age range to go on holiday!!!".format(name))

veg_item = ['beans','carrot','ham','tomato','cauliflower']

nasty_item = ''
def food_stuff():
    for item in veg_item:
        if item == 'ham':
            nasty_item = item
            continue
        else:
            print(item)
food_stuff()

x= 35
x += 5
print(x)

x -= 5
print(x)

x *= 10
print(x)

x /= 10
print(x)
if nasty_item is not None:
    print(nasty_item)
