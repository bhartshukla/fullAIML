# --------------- Exception handling ------ ------- 

# try, except,else,finally


# fir write try and also accept block for perticuler exception -- ex zerodivison error 
# then use else block


try:
    x = int(input("enter x:"))
    ans = 10/x
except ZeroDivisionError:
    print("Divide by 0 is not allowed ")   
except ValueError:
    print("Invalid Input ")
else:
    print(ans) 

finally:
    print("THIS is end")


