def filler(temp, startingday):
    
    while(startingday>=0):
        temp.insert(0,0)
        startingday -=1
    return temp

month = ['Jan','feb','mar','apr','may','june','july','aug','sept','oct','nov','dec']
daysweek = ['mon','tues','wed','thu','fri','sat','sun']
day = 'Mon     Tue     Wed     Thu     Fri     Sat     Sun'
daysinmonth= [31, 28 , 31 , 30 , 31 ,30 ,31 ,31 ,30 ,31 ,30, 31]

sum = 0
temp = []
year = int(input("enter the year...................."))
leap = False
if((year%100==0 and year%400==0) or (year%100!=0 and year%4==0)):

    daysinmonth[1] = 29

sum = int(365.25 * (year-1))+6
startingday = sum % 7


for i in range(0,len(month)):
    weekday = 0
    print("\n-----------------------", month[i],"------------------------\n")
    print(day)
    thismonth = daysinmonth[i]
    s = list(zip[month , daysinmonth])
    
    for j in range(1,thismonth):
        temp.append(j)
        temp = filler(temp,startingday)

   


        
        

