# LIST (Mutable sequence of values)

'''
marks_list =[89,90,89,87,96,45]

print(marks_list)
# print(len(marks_list))

# print(marks_list[4])

marks_list[3] = 99

print(marks_list)

# slicing ---- ------------------------------------

print(marks_list[1:5])
print(marks_list[-6,-3])

'''

# ===========LIST METHODS or functions ++++++ ++++++
'''

l.appaend(val) # add one lement a the end
l.insert(idx, val) #insert element at idx
l.sort()  # arrange in increasing order
l.reverse() #reverses Order

'''

num = [1 ,2,3]
print (num)

# num.append(5)   
# print (num)

# num.insert(2, 6)
# print(num)

nums = [4,6,3,9,2,10]
nums.sort()
print(nums)

nums.sort(reverse=True)
print(nums)

nums.reverse()
print(nums)