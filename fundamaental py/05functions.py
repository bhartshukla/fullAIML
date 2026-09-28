# types of function
# 1) Built in---- print(),  type(), range()
# 2) user defined ----




def hello(): # fnx defination
    print("Hellow")

hello() #fnx call 

def heloo():
    print("HELLO BHARAT")

heloo()   

def sum(a,b):
    sum = a+b
    return sum
print(sum(4,5))     # 4 or  5 are argument



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


# print of factrial of any number

def fact(n):
   fac = 1
   for i in range(1,n+1):
       fac = fac*i

   return fac

# n = int(input("Enter your number : "))
# print(fact(n))