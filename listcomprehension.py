# OUTPUT for item in iterable if condition

number  = []

for i in range(6):
    number.append(i*i)

print(number)


sq = [i*i for i in range(6)]   #// lsit comprehensions
print(sq)
            # output then iterable then condition
sqodd = [i*i for i in range(6) if i%2 != 0] #// lsit comprehensions
print(sqodd)

value = [-2,-4,-5,3,4,-3,5,6]
num = [0 if val<0 else val for val in value]
print(num)



