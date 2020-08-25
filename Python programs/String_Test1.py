
from array import*
import math
input_string = input("Enter a list numbers or elements separated by space: ")
input_string=input_string.replace(" ","")
print(input_string)


# userList = input_string.split()
# print("user list is ", userList)

#rows=5
#cols=5
#print(two_d)
#x=input()
l=len(input_string)
print ("[Lenght of the string= ", l)

#for i in range(l):
 #   print (i,"....", input_string[i])


cols= (l**0.5)
tmp=cols-int(cols)
if (tmp==0.0):
   rows=cols
else:
   rows=cols+1
cols=int(cols)
rows=int(rows)

print ("Rows=", rows,"Cols=",cols)
two_d = [["" for i in range(cols)] for j in range(rows)]

for k in range(l):
    j=int(k%cols)
    i=k//cols
    two_d[i][j]=input_string[k]
   
for i in range(rows):
    for j in range(cols):
        print(two_d[i][j],end="\t")
       
    print()

x=input()
print()
print()
print()

s=""
ch=""
for i in range(cols):
    
    for j in range(rows):
        print(two_d[j][i],end="\t")
        ch=two_d[j][i]
        s=s+ch
        
    s=s+" "  
    print()
    
print(s)
    








    




