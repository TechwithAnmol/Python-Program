from array import*
import math


r=input('Type Row number of   the  Queen....  ')
c=input('Type Column number of the Queen....  ')
r=int(r)
c=int(c)

board = [["O" for ii in range(7)] for jj in range(7)]

for i in range(7):
    for j in range(7):
        if ((i==r) or (j==c) or (abs(r-i)==abs(c-j))):
            board[i][j]='#'
        print(board[i][j],end="\ ")
    print()
    
   
     
         
     
