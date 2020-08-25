t = int(input())
for _ in range(t):
    #n = int(input())
    code = [3,6,5,4,1,2]
    monkey = ['1','2','3','4','5','6']
    num2 = []
    num2 = monkey
    temp =['1','2','3','4','5','6']
   #code = [int(i) for i in input().split()]
   #monkey = [i for i in range(1,n+1)]
    #temp = [0 for i in range(1,n+1)]
    newnum = ''
    counter = 0
    while True:
        print(monkey)
        for i in range(len(code)):
            pos = code[i]
            temp[pos-1] = monkey[i]
        monkey = temp
        print(monkey)
        x = input()
        
        
        
            

    
        
            
    
