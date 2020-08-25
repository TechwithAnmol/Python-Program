n = [1,2,3,5,7,5,7,5,7,4,8,6,7,3,1]
even = []
odd = []
newl = []
for i in n:
        if (i%2==0):
                even.append(i)
        else:
                odd.append(i)
odd.sort(reverse = True)
even.sort()
print(odd)
print(even)
newl.append(even[0])
even.sort(reverse = True)
print(newl)
for i in range(odd):
        if(odd[i]>even[i]):
                print
