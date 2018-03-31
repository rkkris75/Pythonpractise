ipAddress = str(input('Enter IP address please'))
enteredIpAddress = print('IP address enetered is {}'.format(ipAddress))

seg = 1
seg_leng = 0
charc = ''

for charc in ipAddress:
    if charc == ".":
        print("character in the if block with segment is {} and segment length is {}".format(seg,seg_leng))
        seg += 1
        seg_leng = 0
    else:
        seg_leng += 1
        #print("segment is in the else block {} and segment length is {}".format(seg, seg_leng))

if charc != ".":
        print("character is with segment is {} and segment length is {}".format(seg, seg_leng))

# def chall():
#     print(len(ipAddress))
#     for i in range(0,len(ipAddress)):
#         if ipAddress[i] in '0123456789':
#             #print(ipAddress[i],end='')
#             print(ipAddress[i],end='')
#
# chall()