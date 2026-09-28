# # Student enrolments

# given a list of tuples with info(name, sub)

# list all unique course
# list student enrolled in English
# create dictionary (Student , set of courses)

info = [
    ("Alice", "MATH"),
    ("BOB","Science"),
    ("Alice", "Science"),
    ("Charlie", "MATH"),
    ("BOB", "MATH"),
    ("Alice", "ENHLISH"),
    ("Charlie", "ENHLISH")
]

unique_courses = set()

for tup in info:
    unique_courses.add(tup[1])
   
    
# print(unique_courses)

# for tup2 in info:
#     if tup2[1]=="ENHLISH":
#         print(tup2[0])

# for name,couese in info:
#     if(couese == "MATH"):
#         print(name)        


dic = {}

for name, course in info:
    if(dic.get(name) == None):
        dic.update({name: set()})
        dic[name].add(course)
    else:
        dic[name].add(course)    

print(dic)        



