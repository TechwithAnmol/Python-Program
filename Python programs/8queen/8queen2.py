 
def Pause(myprompt):
    print(myprompt)
    aa = input('Press enter to continue')
    return

def queen(i):
    #print('Starting for Quenn No...',i)
    #Pause('')
    j=1
    while j <=8:
        #print('trying to find queen no..',i, 'at colum no. ',j)
        #Pause('')
        if(vacant(i,j) == True) :
            qpos[i] = j
            print('Queen No',i,'Found at(',i,j,')')
            #Print('queen number',i,'=',qpos[i])
            Pause('')
            col[j] = True  
            if i == 8:
                print(qpos)
                Pause('All the queens have been found')
            else:
                #print('calling ',i+1,' Queen') 
                #Pause('')
                queen(i+1)
            col[j] = False
        j =j+1
    Pause('Now back tracking')
    
    return            

def vacant(row,column):
    #Pause('entered in vaccant')
    #print('searching for queen No.',row) 
    t = 0
    ii = 1
    if col[column]==True:
        return False

    while ii <= (row - 1):

        #print('Serching in loop at column= ',ii)
        t = qpos[ii]
        if abs(t - column) == abs(ii - row):
            return False
            break
        ii=ii+1
    #print('exitting vaccant value of check =',check)  
    #Pause('')
        
    return True


        

col = [False for a in range(9)]
qpos = [0 for a in range(9)]
queen(1)    
        

                       
            
            
        
            
            
    
    
