def zhishu(n):
    x = 2
    k = 1
    while k<n:
        x+=1
        for j in range(2,x):
            if x%j==0:
                break
        if j==x-1:
            k+=1
    return x
print(zhishu(2))
