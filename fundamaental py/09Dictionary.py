# Dictionary in python  and they are mutable

# Key:Value Pairs and unorderd 

dict = {
    "name": "BHARAT",
    "agr" : 78,
    "sub" : ["MATH", 'Scinece']
}

dict["agr"] = 9.6

print(dict)
print(type(dict))

print(dict["name"])


#  ================   Dictionary Methods =================

# d.keys()  return all keys 

# d.vlues() return all values

# d.items() return all (Key, val) pairs

# d.get(val)  return val acc. to key

# d.update(new_item)  add new item to dict


print(dict.items())
print(dict.keys())

# print(dict.get("cgpa2"))  # read about .get(val)  and dict[] for getting the value

print(dict.get("m"))   # worng key but is not give error because .get return none 

dict.update({
    "city" : "Lucknow"
})
print(dict)