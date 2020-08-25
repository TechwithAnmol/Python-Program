
from array import*
import math

input_string = input("Enter a list numbers or elements separated by space: ")
input_string=input_string.replace(" ","")
print(input_string)
l=len(input_string)

x=input()
cols= l**0.5
cols=int(cols)
tmp=l/cols
rows=int(tmp+(tmp-int(tmp)>0.0))

print ("Rows=", rows,"Cols=",cols)
two_d = [["" for ii in range(cols)] for jj in range(rows)]

#Storing in Matrix
for k in range(l):
    j=int(k%cols)
    i=k//cols
    two_d[i][j]=input_string[k]
    
#Printing of Matrix
for i in range(rows):
    for j in range(cols):
        print(two_d[i][j],end="\t")
       
    print()#for next Line
    
#for three Blank lines   
print()
print()
#print()

s=""
for i in range(cols):
    for j in range(rows):
        print(two_d[j][i],end="\t")
        s=s+two_d[j][i]
    s=s+" "  
    print()

print(s)
    








    




