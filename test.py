#a=10
#b=15
#print(a/b)

##control flow statements

#name=input("enter the name:")
#if name=="saikiran":
 #   print("hello saikiran")
#else:
 #   print(name,"is wrong user")   if statement is to print valid name
 
#3 if elif else statements

#things=input("enter the brand of electronics:")

#if things=="lg":
 #   print("LG is availble")
#elif things=="aiwa":
 #   print("AIWA is availble")
#elif things=="blue star":
 #   print("BLUE STAR is availble")
#elif things=="redmi":
 #   print("REDMI is availble")
#else: print(things,"stock is  not availble")

#to write biggest numbers
#n1=int(input("enter the first number:"))
#n2=int(input("enter the second number"))
#if n1>n2:
 #   print("enter biggest number",n1)
#else :
 #   print("enter biggest number",n2)  
  
  
### ite rative statements
#for looP
#s="saikiran"
#count=0
#for x in s:
 #   count+=1
  #  print(x) 
#print("the number of characters",count)

#s=input("enter the any string:")
#i=0
#for x in s:
 #   print("for each character in ",i,"is",x)
  #  i+=1
     
##print saikira yadav 10 times using LOOP

#for x in range(10):
 #   print("saikiran yadav")
 
 ###print 0--20 even numbers only
 
#for x in range(21):
 #      if x%2==0:
  #           print(x)   to print 2,4,6,8,10,12,14,16,18,20
  
  #print 0--21 odd numbers
#for x in range(21):
 #         if x%2==1:
  #          print(x)
  
  ###while loop
#x=1
#while x<=10:
 #     print(x)
 
#s="saikirn"
#for x in s:
#      print(x)

#s=input("enter the string:")
#i=0
#for x in s:
 #     print("each char present in ",i,"is",x)
  #    i+=0

###write a pro to find sum of first 'n' number

#n=int(input("enter some number to find sum:"))
#sum=0
#i=1
#while i<=n:
 #     sum=sum+i
  #    i+=1
#print("The sum of first ",n,"number is:",sum)
   
#name=""
#while name!="saikiranyadav":
#      name=input("enter your name to authenticate:")
#print("hello saikiranyadav thank you for authentication ")    #authentication give your name access untill give another is aaccess

### user name and password

#username=""
#password=""
#while username!="saikiran":
 #     username=input("enter the user name:")
#while password!="123456":
 #     password=input("enter your password:")
#print("your username password is activated:")


### identifiers

#a=10
#b=20
#print(id(a))
##print(id(b))     "id" to give  address

#a="saikiran"
#b="deekshith"
#print(type(a)) 
#print(type(b))

 ### datatypes
 
#a=10
#print(type(a))
#b=20.5
#print(type(b))
#c="saikiran yadav"
#print(type(c))
#d=True
#print(type(d))


## slice operation python9                                                                            
      
#lst="This is an index position"
#print(lst)
#print(lst[1:3])
      
#lst=("java","python","ui","red","django","php","sap","visit","linux","mac","ui" ) 
#print(lst)
#print(lst[-1:-6:-2])   to print last index-1 and one missing word and another word print

#lst=("java","python","ui","red","django","php","sap","visit","linux","mac","ui" )
#print(lst[::-2])

#lst=("java","python","ui","red","django","php","sap","visit","linux","mac","ux" )
#print(lst[::2])   
       
#lst=("java","python","ui","red","django","php","sap","visit","linux","mac","ux" )
#print(lst[2::-1])   to print positive index 2 to reverse value print java

#lst=("java","python","ui","red","django","php","sap","visit","linux","mac","ux" )
#print(lst[0::8])  to print first 0 index position and 8 th index position only two positions print

#lst=("java","python","ui","red","django","php","sap","visit","linux","mac","ui" )

#print(lst[1:6:])   1 index to 5th index positions to print

#lst=("java","python","ui","red","django","php","sap","visit","linux","mac","ux" )
#print(lst[::9])

#s="abcdefghijk"
#print(s[4:-2:2])

#s="saikiranyadavjajula"
#print(s[5:-3:2])

#3 input statements 

#x=int(input("enter the  first number:"))
#y=int(input("enter the second number:"))
#print("the sum of two iput numbers are:",x+y)

#x=("2+32+6")
#print(x)sa

#x=eval("10+2+10")
#print(x)

#sai=input("enter the expression:")
#example=eval(sai)
#print(example)

## output statements

# end=" " it  uses in single line comment
# \n   it uses to line brake
#\t  it usse to tab   space 

#print("this is webseries platform")
#print("netflix amazon")
#print("watch web series")

#print("this is webseries platform",end=" ")
#print("netflix amazon", end=" ")
#print("watch web series")


#print("he was going to \n colllege daily")

#print("he was going to \t colllege daily")

#print("he was going to" + " colllege daily")

#print("he was going to " ,"colllege daily")

#print("visual effects" *4)

#a,b,c=10,20,30
#print("value is:",a,b,c)
#a,b,c=10,20,30
#print("value is :",a,b,c,sep="%")

