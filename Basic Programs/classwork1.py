# 07-01-2021 classwork


# # to find the sum of characters ascii values in String list
# l = ["ABC", "xyz"]
# newList=[]
# for i in l:
#     j=0
#     count=0
#     for j in i:
#         count = count + ord(j)
#     newList.append(count)

# print(newList)







# #print strings with repetitive occurrence of an element in list
# l = ["hello", "hi", "lmao", "deep"]
# s = []
# for i in l:
#     count=0
#     for j in range(0,len(i)-1):
#         if i[j] == i[j+1]:
#             count += 1
#     if count>0:
#         s.append(i)
# print(s)






#most frequent words in a list
s = ["hello", "goodday", "goodnight", "hello", "tomorrow"]
l = {}
for i in s:
    if i in l:
        l[i] += 1
    else:
        l[i] = 1
print(l)