
from array import*
import math
input_string = input("Enter a list numbers or elements separated by space: ")

# userList = input_string.split()
# print("user list is ", userList)

#rows=5
#cols=5
#print(two_d)
#x=input()
l=len(input_string)
print ("[Lenght of the string= ", l)

#for i in range(l):
    #print (i,"....", input_string[i])


rows= (l**0.5)
tmp=rows-int(rows)
if (tmp==0.0):
    cols=rows
else:
    cols=rows+1
cols=int(cols)
rows=int(rows)
#print ("Rows=", rows,"Cols=",cols)
two_d = [["" for i in range(rows)] for j in range(cols)]
for k in range(l):
    j=int(l%cols)
    i=l//cols
    two_d[i][j]=input_string[k]
    
print(two_d)







    




