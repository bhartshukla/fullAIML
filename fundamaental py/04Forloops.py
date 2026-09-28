# For Loop generly use for sequential Traversal

string = "Bharat"

# # in => Membership Operator

# for var in string:
#     print(var)



# for i in range(10):
#     print(i+1)


word = "BHARATAAAAAAAAAAAAA SHUKLA JI"

# count the number of A

count = 0
for ch in word:
    if(ch == "A"):
        count = count+1
# print(count)        
    

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


# print the sum of n natural number

# n = int(input("Enter your number"))
n =10

sum = 0

for i in range(1,n+1):
    sum = sum+i

print(sum)    

