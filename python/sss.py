from itertools import permutations
while 1:
    n=input()
    a=[1]*(n-1)
    b=[-1]*(n-1)
    c=a+b
    all_list=list(set(list(permutations(c))))
    for x in all_list:
        s=1
        i=0
        while s>=0 and i<2*n-2:
            s+=x[i]
            i+=1
        if i==2*n-2:
            y=x
            print('('+''.join(['(' if z==1 else ')' for z in x])+')')
