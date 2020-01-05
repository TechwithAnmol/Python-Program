def recurse(n):
    if n == 1:
        return n
    else:
        return n*recurse(n-1)
    
num = int(input('enter the number'))
print('the factorial of the number is',recurse(num))
    