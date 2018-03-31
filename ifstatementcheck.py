# name = input("What is your name?")
# age = int(input("Enter your age {0}".format(name)))
# print(age)
#
# if age >= 18:
#     print('You are eligible to vote')
# else :
#     print('you are not eligible to vote. Please come back after {0} years'.format(18-age))

print("please guess the number between 1 to 20")
guess = int(input())

if guess < 5:
    print("please guess higher")
    guess = int(input())
    if guess == 5:
        print('Well done, you guessed correctly')
    else:
        print('sorry you guessed wrong')
elif guess > 5:
    print("Please guess lower")
    guess = int(input())
    if guess == 5:
        print('well done, you guessed correctly')
    else:
        print('sorry you did not guess correctly')
else:
    print('well done you guessed at the first attempt')
