

import math

string = input()
p = list(string)
for i in p:
    if i == ' ':
        p.remove(i)
#print(p)
leng = len(p)
leng = leng**0.5
x = int(leng)
if (leng - x > 0.0):
    row = int(leng)
    col = row + 1
else:
    row = int(leng)
    col = row
mat = []
for i in range(0,len(p), row):
    rr = p[i:i+row]
    mat.append(rr)
print(mat)



 

    
print(leng , row , col)














#   for i in range(0,len(p), row):
    
  #      mat = [[p[k] for j in range(row)]for i in range(col)]
   #     k = k + row
#print(mat)




#for k in range(len(p)):
 #   for i in range(row):
  #      mat.append(p[k])
   #     for j in range(col):
   #         mat.append([p[k]])
#print(mat)



 
