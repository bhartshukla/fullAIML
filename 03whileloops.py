"""
LOOPS IN PYTHON
---------------
This file demonstrates the use of:
1. while loop
2. for loop (concept mention)
3. break statement
4. continue statement
"""

# ----------------------------------------
# Infinite Loop Example
# ----------------------------------------
"""
This loop runs forever because condition is always True.
Use carefully, otherwise program will hang.
"""
# while True:
#     print("Hello world")


# ----------------------------------------
# Counter Example (Print message 5 times)
# ----------------------------------------
"""
This loop prints "hello Bharat" with a counter value from 1 to 5.
"""
counter = 1   # iterator initialization

while counter <= 5:
    print("hello Bharat", counter)
    counter += 1   # increment


# ----------------------------------------
# Print numbers from 1 to 10
# ----------------------------------------
"""
This loop prints numbers from 1 to 10.
"""
count = 1

while count <= 10:
    print(count)
    count += 1


# ----------------------------------------
# Print numbers in reverse (10 to 1)
# ----------------------------------------
"""
This loop prints numbers from 10 down to 1.
"""
count = 10

while count >= 1:
    print(count)
    count -= 1


# ----------------------------------------
# Multiplication Table Program
# ----------------------------------------
"""
This program takes user input and prints its table from 1 to 10.
Runs continuously using an infinite loop.
"""
while True:
    num = int(input("Enter Your Number: "))
    i = 1
    while i <= 10:
        print(num * i)
        i += 1


# ----------------------------------------
# Break Statement Example
# ----------------------------------------
"""
Loop runs from 1 to 10 but stops when number is divisible by 6.
'break' exits the loop immediately.
"""
j = 1

while j <= 10:
    if j % 6 == 0:
        break
    print(j)
    j += 1

print("outside the Loop")


# ----------------------------------------
# Continue Statement Example
# ----------------------------------------
"""
Loop from 1 to 10:
- Skips numbers divisible by 3
- Prints remaining numbers
'continue' skips the current iteration.
"""
l = 1

while l <= 10:
    if l % 3 == 0:
        l += 1   # important to increment before continue
        continue
    print(l)
    l += 1