# For Loop generly use for sequential Traversal

# string = "Bharat"

# # in => Membership Operator

# for var in string:
#     print(var)



# for i in range(10):
#     print(i+1)


'''

word = "BharatShukla"
count = 0
for ch in word:
    if(ch =='a'):
        count+=1

print("Count of a is : ", count)        

'''

'''
# print vowel count of a given String

word = "BharatShuklajiis a good boy"
count =0
for ch in word:
    if(ch=='a' or ch=='i' or ch=='e'or ch=='o' or ch=='u'):
        count+=1
        print(ch , count)
print(count, "these numbers of vowel")      

'''

# range function range(start, stop, step)

'''

for r in range(6):
    print(r) 


for r in range(1,6):
    print(r)


for r in range(1,6,2):
    print(r)

    '''


# print the sum of n naturan number

sum = 0

for num in range(11):
    sum = sum+num
    print (num, "its sum is :", sum)

