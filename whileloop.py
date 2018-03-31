# i = 1
# while i <= 20:
#     print("i's value now is {}".format(i))
#     i += 1

available_exits = ['north','east','north east','west']

chosen_exit = ""

while chosen_exit not in available_exits:
    print("You are not near exit")
    chosen_exit = input("please chose the exit")


print("You are out of the exits now!!!")