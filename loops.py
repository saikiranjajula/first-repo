##iterative statements
#1.for loop
#while loop

#1.for loop:
#s="saikiran"
#for x in s:
#    print(x)


#s="saikiran"
#count=0
#for x in s:
 #   count+=1
  #  print(x)
   # print("the number of characters ",count)
   
##even numbers
#for i in range(21):
 #   if i%2==0:
  #      print(i)
  
  ##odd numbers
  
#for i in range(21):
#      if i%2==1:
 #         print(i)
 
#n=input("enter the string:")
#i=0
#for x in n:
 # print("each character ispresent in",i,"is",x)
 
  #i+=1
  
##write a program 1 to 10 numbers decending order in for loop "assinment" 21-06-23

#for i in range (10,0,-1) :
 #     print(i,end=",") i=10
 

##write a program to sum the values the given from the keyboard  
#num=int(input("entr the numnber:"))
#sum=10
#for i in range(num+1):
 # sum=sum+i
 # i=i+1
  #print(sum)
  
  ### while loop: a while condition is true  and body will excuted the condition is false
  
#n=int(input("enter the number :"))
#sum=0
#i=1
#while i<=n:
 ## sum=sum+i
  #i+=1
#print("the sum of given numbers is",n,"is",sum)

#print 5 times name positive or assending order
#i=1
#while i<=5:
#      print("saikiran")
 #     i=i+1
 
#i=5
#while i>=1:
 #     print("1,2,3,4,5")
 #     i=i-1 
 
 ##print saikiran 5 time and jajula 4 time
#i=1
#while i<=5:
3#      print("saikiran",end="")
#      j=1
#      while j<=4:
#            print("jajula",end="")
#            j=j+1
#      i=i+1
#      print()



#write program "only when usernme and password" is correct then only the out should be thank you for authentication

#name=""
#password=""
#while name!="saikiran" or password!="123456":
      
 #    name=input("enter your username :")
  #   password=input("enter your password :")
#print("hello",name,"your login access is perimited")
            
#####################
# for i in range(3):
#      username=input("enter your username:")
#      password=input("enter your password :")
#      if username=="saikiran" and password=="sai1234":
#            print("access perimited")
#            break;
#      else:
#            print("access deinied")
#      print("try again")
# else:
#      print("no more attempts tha for day")

#print table

#a=int(input("enter the table :"))
#i=1
#while(i<11):
#      print(a,'*',i,'=',a*i)
#      i=i+1

##########################
#nested loop

#for i in range(4):
 #     print(i)

#for i in range(4):
#      for j in range(4):
#            print("i={} and j={}".format(i,j))
########
#produce the following pattern   
#for i in range(6):
 #          for j in range(6):
  #           if i>=j:
   #            print(chr(65+j)+'',end="")
    #       print()
    
### enter row and columns

#for i in range(1,10):
#  print(i)    # to print output line by line

#for i in range(1,10):
 # print(i,end=" ")    # to print output single line horizental
 #####
 
#rows=int(input("enter no of # rows :"))
#columns=int(input("enter number # of columns :"))
#symbols=input("enter the symbol :")
 
#for x in range(rows):
#      for y in range(columns):
#        print(symbols,end="")
#      print()

##

# a=int(input("enter no of rows"))
# #b=int(input("enter no of columns"))

# for i in range(a):
#     for j in range(i+1):
#         print(j,end=" ")
#     print()


    
# for i in range(3):
#   for j in range(3):
        
#       print(j,end=" ")
#       print(=
    
### print number pattern

# for i in range(4):
#   for j in range(i+1):
#     print()    

### increasing pattern

n=5
for i in range(n):
  for j in range(i+1):
      print("*",end='')
  print()
  
## decreasing pattern
n=6
for i in range(n):
  for j in range(i,n):
        print('#',end='')
  print()
### right side pattern

n=5
for i in range(n):
      for j in range(i,n):
            print('',end=' ')
            
      for j in range(i+1):
            print('*',end='')
      print()
      
## left side payttern

n=5
for i in range(n):
      for j in range(i+1):
            print('',end='')
      for j in range(i,n):
            print('#',end='')
      print()
      
## hill pattern

n=5
for i in range(n):
      for j in range(i,n):
            print(' ',end=' ')
      for j in range(i):
            print('*',end=' ')
      for j in range(i+1):
            print('*',end=' ')
      print()
      
 #---------------     
### reverse hill pattern


n=5
for i in range(n):
      for j in range(i+1):
            print(' ',end=' ')
      for j in range(i,n-1):
            print('$',end=' ')
      for j in range(i,n):
            print('$',end=' ')
      print()
  
## diamond pattern 

n=5
for i in range(n):
      for j in range(i,n):
            print(' ',end=' ')
      for j in range(i):
            print('#',end=' ')
      for j in range(i+1):
            print('#',end=' ')
      print()
      
      n=5
for i in range(n):
      for j in range(i+1):
            print(' ',end=' ')
      for j in range(i,n-1):
            print('#',end=' ')
      for j in range(i,n):
            print('#',end=' ')
      print()
      
### Multiplication table pattern

rows=10


for i in range(1+rows):
      for j in range(1,i+1):
            print(i*j,end=' ')
      print()
####  hill pattern2
n=5

for i in range(n):
      for j in range(i,n):
            print(' ',end=' ')
      for j in range(i):
            print('*',end=' ')
      for j in range(i+1):
            print('*',end=' ')
      
      print()      