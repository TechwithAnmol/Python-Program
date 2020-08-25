def hello(x):#x is a function taken as an arguement
    def inner(a,b):#changable function(wrapper function)
        if a < b:
            a,b = b,a
            return x(a,b) #calling the actual function
        else:
            return x(a,b)
    return inner
def div(a,b): #normal divide
    print(a/b)
div = hello(div)#declaring decorator
div(int(input()),int(input()))#calling function

