for i in range(3):
     username=input("enter your username:")
     password=input("enter your password :")
     if username=="saikiran" and password=="sai1234":
           print("access perimited")
           break;
     else:
           print("access deinied")
     print("try again")
else:
     print("no more attempts tha for day")
