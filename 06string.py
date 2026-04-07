# string in puthon is immutable

word ="Hello String"
word2 = "in pyhton"
# print(len(word))

#concatnate
# print(word + " " + word2)

# print(word[2])

# for ch in word:
    # print(ch)


####### ----- Slicing the String -------

# str[statring index and ending index (where ending index not encluded)]

name = "Hello bharat"

# print(name[3:9+1]) 

# negative indexing ----

# print(name[-6:-1])




# String formatting ==----===----

a = 5
b= 10
sum = a+b

# normla formatting
print("language is {}".format("python"))
print("som of {} & {} is {}".format(a,b,sum))

# index based formatting 

print("sum of {1} & {0} is {2}".format(a,b,sum))


# value based formatting 
print("values of vars {a} & {b}".format(a=10,b=20))

 
# F-string --- formatting  it use Literal string interpolation

print(f"sum od {a} & {b} is {a + b}")