# ipaddress = input("Please enter the ipaddress")
# per_check = ipaddress.count('.')
# print(type(per_check))
# print("Number of periods in the ip address is {}".format(per_check))

# even = [2,4,6,8]
# print("Even variable list is {}".format(even))
#
# even2 = even
# print("Even2 variable list is {}".format(even2))
#
# even2.sort(reverse=True)
#
# print("Even is {} and Even2 is {}".format(even, even2))

# even = [2, 4, 6, 8]
# even2= list(even)
# even3 = even
#
# print("Even to even2 chcek with is check", even is even2)
# print("Even to even2 chcek with double equal", even == even2)
# print("Even to even3 chcek with is check", even is even3)
# print("Even to even3 chcek with double qual", even == even3)
# even3.sort(reverse=True)
# print("Even to even2 chcek with double equal, post sort fucntion call", even == even2)
# print("Even is {} and Even2 is {}, Even 3 is {}".format(even, even2, even3))

# even = [2,4,6,8]
# odd = [1,3,5,7,9]
#
# new_num = even,odd
# new_num1 = [even,odd]
# #new_num2 = {even,odd}
# print("new_num is {}, new_num2 is {}".format(new_num,new_num1))
#
# for number_set in new_num1:
#     print(number_set)
#
#     for val in number_set:
#         print(val)

# pets = []
# pets.append(['Dog','Cat','Fish','Tiger'])
# pets.append(['Dog','Fish'])
# pets.append(['Tiger','Cat','Fish'])
#
# #print(pets)
#
# for pet in pets:
#     #print("In the for loop",pet)
#
#     if 'Tiger' not in pet:
#         print("In the if loop",pet)
#         for dom_pet in pet:
#             print("Domestic pet is ", dom_pet)

string1 = 'My name is Rajesh'
string2 = len(string1)

print(string2)
print(string1)
# for val in string:
#     print(val)
my_iter = iter(string1)
for i in range(1,string2):
    for my_iter1 in my_iter:
        print(my_iter1)

