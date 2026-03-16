# Variable 

name  = "bharta"
age = 30
PI = 3.14

print ("my name is ", name )
print ("my age is ", age )

print(PI-4)

print (name , age, PI)


# Data TYPES

# Integer , String , Float , Boolean , None

print (type(age))



'''
Mulitline comment

'''

# Operators 

# Arithmetic ( +,-,*,%,**) , Relational / Comprasion ( >=,>, <= , < , == , !=), Assignment (= , +=, ) , Logical (NOT , OR , AND)

a = 5

a += 4 # a = a+4

print(not (5>8)) #true
 
print((5>4) and (4>8)) # false 

print((5>4) or (4>8)) #true

# Bitwise 
# Membership 

'''

## Operator Precedence ====----- 
()
**
*,/,%
+,-

==, !=, >, >=, <, <=

not 
and 

or

'''

# Type Conversion  ------ compatible type 

# Type Conversion (implicit - automatic by pyhton )

ans  = 5  + 10.0  # ans  = 15.0 which is float value 

print (type(ans))


# Type Casting (Explicit - done by developer)

ans2 = int(10+10.3)
print(type(ans2))


# User input -----------

a = input("Enter your value : ") #string input by deafult 

# print(a) 


nums1 = int(input("Enter your num1"))
nums2 = int(input("Enter your num2"))

sum=(nums1+nums2)
print(sum)

