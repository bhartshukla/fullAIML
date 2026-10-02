# reading [default] -- r

# writing, truncates file first - overwrite -- w

#   Create new and open for writing -- x

# writing, appends ate end  -- a

# binary mode -- b

# text mode [default] -- t

# opens disk file for update (r & w) -- + 


file = open("demo.txt" ,"a") # append the this text with existing text
file.write("hello barat\n new append line ")
file.close()

file2 = open("demo2.txt", "x") # create a new file
file2.write("Some random text\n bharat shukla python")
file2.close()                      


# x -> Create only
#     file already exists -> Error

# w -> Write
#     file doesn't exist -> Create
#     file exists -> Overwrite


# "rt"  # read text
# "rb"  # read binary

# "wt"  # write text
# "wb"  # write binary

# r+
# w+
# a+

