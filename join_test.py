# from functools import reduce
#
# sentence = ['this','is','a','sentence']
#
# out_str=str(reduce(lambda x,y:x+","+y,sentence))
#
# print(out_str)

sentence = ['this','is','a','sentence']
s1 = " "
s=(s1.join(sentence))
print(s)

words = ['aba', 'xyz', 'xgx', 'dssd', 'sdjh']
str_join = 'Test'

for i in words:
    print(str_join+i)