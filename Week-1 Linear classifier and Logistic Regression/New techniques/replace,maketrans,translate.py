import string
""" 
1) replace --> Does a substring replace 
It tries to match entirely first arguement as one chunk and replace it with the entirely of the second argument
"""
print("1 --> Normal Replace function")
str1="Hello: that is Prashanth"
print(str1.replace("that","this"))
print(str1.replace(':',','))  
print()
"""
2) maketrans() + translate() --> Does a character level transalation
It replaces individual character from the first argument with the corresponding character in the second
maketrans(x,y=None,z=None) --> Return a translation table usable for str.translate()  """

print("2 --> Using maketrans() + translate()")
"""
i) string.maketrans(dict1)
If there is only one argument, it must be a dictionary mapping
key   --> Unicode ordinals (integers)/ characters 
value -->  Unicode ordinals,string,None  """
print("1 argument")
string = 'Hari balloon'
dict1  = {"a":"1","b":"2"}       # or  dict1={97:1,98:2}
table  = string.maketrans(dict1) # t --> translation table  (Which character to be replaced by new character)
print(table)   					 # {97: '1', 98: '2'}
print(string.translate(table))   # H1ri 21lloon

string = 'Hi Sam'
x = 'mSa'
y = 'eJo'
table  = string.maketrans(x,y)
for i,j in zip(x,y): print(i,ord(i),j,ord(j))  # All the charcaters:replacing character are converted into ASCII
print(table) 				   # {109: 101, 83: 74, 97: 111}  
print(string.translate(table)) # replacing the values from the table (left to right i.e 109 is replaced by 101) and the corresponding character is returned

""" 
ii) string.maketrans(str1,str2)
If there are two arguments, they must be strings of equal length, and in the resulting 
dictionary, each character in x will be mapped to the character at the same position in y.
"""
print("2 arguments")
string="This is super Mario"
str1  = 'abcdef'
str2  = '123456'
table = string.maketrans(str1,str2)  # [a:1,b:2,c:3,d:4,e:5,f:6] (All are representd in unicode format)
print(table)
print(string.translate(table))

"""
iii) string.maketrans(str1,str2,str3)
If there is a third argument, it must be a string, whose characters will be mapped to None in the result.
"""
print("3 arguments")
string="(Hello# Ever%yone! this is Mario???"
str1  = 'abcdef'
str2  = '123456'
str3  = '#%!?'
table = string.maketrans(str1,str2,str3)
print(table)  # {97: 49, 98: 50, 99: 51, 100: 52, 101: 53, 102: 54, 35: None, 37: None, 33: None, 63: None
print(string.translate(table))
