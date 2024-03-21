n=input()
def f(k):
    if k>2:
        return f(k-1)+f(k-2)
    elif k==1:
        return 1
    elif k==2:
        return 1
print f(n)
