tup = (1,2,3,4,5, "abc", "34") 

# tuples are immutable in python /

print(tup)
print(type(tup))
print(len(tup))

print(tup[3])


print(tup[2:4])

tup2 = (1,)  # single vlaue tuple is use comma after one value

for v in tup:
    print(v)


tup1 = (1,2,3,4,5,6 ,5 ,3 ) 

sum = 0

for i in tup1:
    sum+=i

print(f"sum of all value of tuple is {sum}")    



# ==========  Tuples methods +++++++=======

# t.index(val)   returns 1st occurence idx
# t.count(val)   counts total occurance 


tup3 = (1,2,3,4,5,6 ,5 ,3,2,3,2 ) 

print(tup3.index(2))
print(tup3.count(2))