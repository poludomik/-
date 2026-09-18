def f(n):
    res = 0
    for i in range(len(n)):
        res += n[i]*22**(len(n)-1-i)
    return res
for x in range(21, 1, -1):
    a = [1,2,3,1,3,x,5,7]
    b = [1,x,3,4,5,6,1]
    if (f(a)+f(b))%21==0:
        print((f(a)+f(b))/21)
    

    
    
