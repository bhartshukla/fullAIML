# Dictionary in python  and they are mutable

# Key:Value Pairs

dict = {
    "NAME": "Bharat",
    "cgpa": "9.2",
    "sub": ["phy", "cs"],
}

# DICT["cgpa"] = 9.7
# print(type(DICT))

# print(DICT["cgpa"])

dict_keys = dict.keys()
print(dict_keys)
print(type (dict_keys))

dict_keys = list(dict.keys())

print(dict_keys)
print(type (dict_keys))


dict_values = dict.values()
print(dict_values)


#  ================   Dictionary Methods =================

# d.keys()  return all keys 

# d.vlues() return all values

# d.items() return all (Key, val) pairs

# d.get(val)  return val acc. to key

# d.update(new_item)  add new item to dict


print(dict.items())

print(dict.get("cgpa2"))  # read about .get(val)  and dict[] for getting the value


dict.update({
    "city" : "Lucknow"
})
print(dict)