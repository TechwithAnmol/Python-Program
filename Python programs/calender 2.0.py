month = ['Jan','feb','mar','apr','may','june','july','aug','sept','oct','nov','dec']
daysweek = ['mon','tues','wed','thu','fri','sat','sun']
day = 'Mon     Tue     Wed     Thu     Fri     Sat     Sun'
daysinmonth= [31, 28 , 31 , 30 , 31 ,30 ,31 ,31 ,30 ,31 ,30, 31]
year = int(input("enter the year...................."))
sum = int(365.25 * (year-1))+6
startingday = sum % 7
if((year%100==0 and year%400==0) or (year%100!=0 and year%4==0)):
    daysinmonth[1] = 29


for k in range(len(month)):
    print("\n-----------------------", month[k],"------------------------\n")
    print(day)
    c = 0
    current = 0
    temp = 0


    for i in range(6):
        for j in range(7):
            c+=1
            if(c == daysinmonth[k]):
                temp = j
            if (c<=startingday or c - startingday>daysinmonth[k]):
                print(" ",end = '\t')
            else:
                print(c - startingday, end = '\t')
        
        
        print()
    print(temp)
    startingday = temp + 1
    
    
