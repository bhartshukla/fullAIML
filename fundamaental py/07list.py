# LIST (Mutable sequence of values)

# marks = [99,33,56,78,89,"APPLE", 10.99]
# print(marks)
# print(marks[2])
# print(len(marks))

# marks[2] = 78
# print(marks)

# print(marks[1:6])





# ===========LIST METHODS or functions ++++++ ++++++
'''

l.appaend(val) # add one element a the end
l.insert(idx, val) #insert element at idx
l.sort()  # arrange in increasing order
l.reverse() #reverses Order

'''

num = [1 ,2,3]
print (num)

num.append(4)
print (num)

num.insert(1,6)
print (num)


num2 = [3,4,2,9,5]
num2.sort()
print(num2)

# num2.sort(reverse=True)
# print(num2) 

num2.reverse()
print(num2)




# ========== List with loops ===================

numb = [3,4,5,6,72,3,4]  # [linear search]

# for num in numb:
#     print(num)

n = 0
v = 72
for i in numb:
    if (i == v):
        print(f"{v} at index {n}")
        break
    n+=1
        
