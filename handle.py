import json

# json.loads() # s stand for string
# json.dumps()  # json string in python 


# json.load()
# json.dump()

# json_str = '{"name" : "Bharat", "isTeacher" : true}'

# py_obj = json.loads(json_str)

# print(type(py_obj))
# print(py_obj)

# py2_obj = {
#     "name" : "Bharat",
#     "isTeacher" : True
# }

# json2 = json.dumps(py2_obj)
# print(json2 , type(json2))


d = {
    "star" : "bharat",
    "agr" : 33,
    "myplace" : None
}

# with open("fullAIML/data.json", "r")as f:
    # pyobj = json.load(f)
    # print(pyobj , type(pyobj))

with open("fullAIML/data.json", "w") as f:
    json.dump(d, f, indent=4, sort_keys=True) 

    # its chnage and overwrite the old data 



