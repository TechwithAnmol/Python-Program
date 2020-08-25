
def Pause(myprompt):
    print(myprompt)
    aa = input('Press enter to continue')
    return
def queen(i):
   # print(i)
   # Pause('Entered in function queen for solution No..')
    j=1
    while j <=8:
        #print('trying to find queen no..',j)
        #print (j)
        if(vacant(i,j)):
            qpos[i] = j
            #print('(',i,j,')','at column=',j)
            #rint('queen number',i,'=',qpos[i])
            #Puse('')
            col[j] = True  
            if i == 8:
                print(qpos)
                #pause('All the queens have been found')
            else:
                print('calling ',i+1,' Queen') 
                Pause('')
                queen(i+1)
            col[j] = False
    j += 1
    
    return            

def vacant(row,column):
   # Pause('entered in vaccant')
    print('searching for queen No.',row)
    check = True   
    check = not(col[column])
    t = 0
    ii = 1

    while ((ii <= row - 1) and (check) ):
        t = qpos[ii]
        if abs(t - column) == abs(ii - row):
            check = False 
        ii=ii+1
    print('exitting vaccant value of check =',check )  
    Pause('')
        
    return check

        

col = [False for a in range(8)]
qpos = [0 for a in range(8)]
queen(1)    
        

                       
            
            
        
            
            
    
    
