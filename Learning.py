import string
str1 = 'Hi Hello everyone, Hi How are You you???'

def Remove_Punctuation(str1):
    for i in str1:
        if i in string.punctuation:
            str1 = str1.replace(i,' ')
    return str1

str1  = Remove_Punctuation(str1)
print(str1)
##############################################
def Count_words(str1):
    str1 = str1.split()
    list1 = []
    for i in str1:
        list1.append(str1.count(i))
    return (set(zip(str1,list1)))

count = Count_words(str1)
print(count)
##############################################

# Using str.maketrans tool
intab = 'Prashanth'
outab = '123456789'

transtab = str.maketrans(intab,outab)
str1='chandler drickh'

print(str1.translate(transtab))

#########
# Dealing with ASCII values
str1 = '!@Pr@sh@nth ?? Hi* Hell????o'
dict1 = str.maketrans({ key:None for key in string.punctuation })
print(str1.translate(dict1))

#The overall beauty is that all the special characters are removed, and the remaining text is self alligned
##############################################