cube = lambda x: x**3# complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    l=[]
    for i in range(n):
        if i<=1:
            l.append(i)
        else:
            l.append(l[i-2]+l[i-1])
    return l
