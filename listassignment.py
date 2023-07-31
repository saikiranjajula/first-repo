######## list compression3
# w=['AMAN','SRIHARI','SAI','RAM']
# n=[i for x in w for i in x]
# print(n)

################################# list functions assignment##
##-1:-take a list of values and check weather given number is present the list or not , if present 
#expected output should be 10 is available and first occurence is at : index "25-07-2023"
def find_number_in_list(lst,number):
    if number in lst:
        first_occurrence_index=lst.index(number)
        return f"{number} is availble,and its first occurence is at index {first_occurrence_index}."
    else:
        return f"{number} is not in list."
lst=[1,2,3,4,5,6,7,10,20,30,40,50,10]
search_number=10
result=find_number_in_list(lst,search_number)
print(result)

    
########## take a list of elements from 1 to 50 when ever user enter the value from 1- 50 particular elements needs to removed 
#n=int(input("enter the number :"))   "to use remove function"
# list1=[i for i in range(1,51)]
# list2=[]
# x=int(input("Enter the loop Number"))
# while (x>0):
#     n=int(input("Enter a number to be Removed"))
#     if (n<50 and n>0):
#         if(n in list2):
#           print("Sorry this number is already removed",n)
#         else:
#           if (n in list1):
#              list2.append(n)
#              list1.remove(n)
#              print("The Number is removed",n)
#              print(list1)
#              print(list2)
#           else:
#             print("The value ",n,"is not Present in the List1")
#     else:
#       print("The number is Not allowed",n)
#     x=x-1
    
############  list comprehension assignment
#1.program to display vowels present in the user-input
###########

vowels=['a','e','i','o','u']
list=input("enter the word search here :")
found=[]

for x in list:
    if x in vowels:
     if x not in found:
      found.append(x)
print(found)
print("the no vowels present in word",list,"is",len(found))