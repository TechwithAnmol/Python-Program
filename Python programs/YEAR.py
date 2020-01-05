days =['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
month = [31,28,31,30,31,30,31,31,30,31,30,31]
yy = int(input('enter the year you wanna search'))
sum_year = 0
sum_year = (yy-1)*365.25
sum_year = int(sum_year)
if (yy%4==0):
    month[1] = 29
mm = int(input('enter the month you wanna search'))
mm = mm-1
for i in range(0,mm-1):    
    sum_month = 0
    sum_month = sum_month + month[i]
sum_day = int(input('enter the day you wanna search'))
totalsum = sum_month + sum_year + sum_day
totalsum = totalsum-2
r = totalsum%7 
print(days[r])   
