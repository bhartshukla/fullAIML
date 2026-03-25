# types of function
# 1) Built in----
# 2) user defined ----




def hello(): # fnx defination
    print("Hellow")

hello() #fnx call

'''

def sum (a,b):
    s = a+b
    return s

ans = sum(4,5)
print(ans)

'''

# avg calculate 

'''
def avg(a,b,c=2):
    av = (a+b+c)/3
    return av

a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))
c = int(input("Enter the value of c : "))

ans = avg(a,b,c)
print(ans , "Its your avg ")

'''



# Lambda Function -- uses in high order function

sum = lambda a,b: a+b
print(sum(3,4))