import random

print("Please type 0 at any point to exit the game")

lowest_num = int(input("Please enter the lower number"))
highest_num = int(input("Please enter the higher number"))

print("Please guess the number between {} and {}".format(lowest_num,highest_num))
guess_num = 0

corr_num = random.randint(lowest_num,highest_num)

print(corr_num)

#print("Random generated number is {}".format(corr_num))
quit_res= ""
while guess_num != corr_num:
    #print("You have guessed incorrectly, please try again")
    #print("Random generated number in while loop is {}".format(corr_num))
    print("Please enter the number now!!!")

    guess_num= int(input())
    if guess_num == 0:
        print("Do you want to quit the game?, type Y")
        quit_res = input()
        if quit_res == 'Y':
            break
    elif guess_num > corr_num:
        print("Guess Lower")
    elif guess_num < corr_num:
        print("Guess Higher")
    # if guess_num != corr_num:
    #     print("You have guessed incorrectly, Please try again")


if quit_res != 'Y':
    print("You have guessed correctly")
else:
    print("You are out of the game now")

