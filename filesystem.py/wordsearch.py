data=True
line = 1

with open("demo.txt", "r") as f:
   while data:
      data = f.readline()

      if("good" in data):
        print("word found at line ", line )
        break
    #   print(data)
      line+=1

     