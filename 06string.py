'''
STRING IN PYTHON (IMMUTABLE)
- Strings cannot be changed after creation
- Any modification creates a new string
'''
word = "Hello String"
word2 = "in python"

# print(len(word))   # length of string


'''
STRING CONCATENATION
- Joining two or more strings using +
'''
# print(word + " " + word2)


'''
STRING INDEXING
- Access characters using index (starts from 0)
'''
# print(word[2])   # l


'''
ITERATING THROUGH STRING
- Loop through each character
'''
# for ch in word:
#     print(ch)


'''
STRING SLICING
- Extract part of string
- Syntax: str[start : end] (end not included)
'''
name = "Hello bharat"

# print(name[3:10])   # lo bhar


'''
NEGATIVE INDEXING
- Starts from end (-1 is last character)
'''
# print(name[-6:-1])   # harat


'''
STRING FORMATTING
- Used to insert values into string
'''
a = 5
b = 10
sum = a + b


'''
NORMAL FORMATTING (.format())
'''
print("Language is {}".format("python"))
print("Sum of {} & {} is {}".format(a, b, sum))


'''
INDEX-BASED FORMATTING
- Use index positions
'''
print("Sum of {1} & {0} is {2}".format(a, b, sum))


'''
VALUE-BASED FORMATTING
- Use variable names
'''
print("Values of vars {a} & {b}".format(a=10, b=20))


'''
F-STRING FORMATTING (BEST & MODERN)
- Easy and readable
- Directly use variables inside {}
'''
print(f"Sum of {a} & {b} is {a + b}")