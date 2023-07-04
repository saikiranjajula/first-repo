### Transform statements
#1.brake     :brake means entire execution stop a loop
#2.continue  :contnue means it will go back  to the loop
#3. pass     :if you want empty provide empty body then go for statement

#             :-do nothing

#1. brake:
# for i in range(10):
#     if i==6:
#         break
#     print(i)

# ex:--
name="saikiran"
for i in name:  
    if i!=i:
        continue
    print(i)     

# ex:-2
# cart=[10,20,600,70,80,90]
# for item in cart:
#     if item>500:
#         print("sorry wecannot procees this order.. insurence require")
#         break
#     print("process order:",item)

 #2.continue:
# for i in range(10):
#     if i==6:
#         continue
#     print(i)

# for i in range(10):
#    if i==5 or i==7:
#         continue
   
#    print(i)
#ex-3
# cart=[10,20,600,70,80,90]
# for item in cart:
#     if item>500:
#         print("sorry we cannot find thi order")
#         continue
#     print("process this order",item)

# ex-4
numbers=[10,20,30,0,40,60,0,80,25]
for n in numbers:
    if n==0:
        print("hey how can devided with zero")
        continue
    print("100/{}={}".format(n,100/n))
        

#3.pass statement

# for i in range(10):
#     if i%2==0:
#         print(i)
#     else:
#         pass   # to print even nbrs otherwise else block is empty
        
# for i in range(10):
#     if i%2==0:
#         pass
#     else:
#         print(i)     # to print odd nbrs otherwise if block is empty :-pass is empty body

