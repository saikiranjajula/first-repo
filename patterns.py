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
      
      ###
      n==5
      for i in range(n):
            p=1
            for j in range(i,n):
                  print(p,end=' ')
                  p+=1
            print()