number=raw_input()
m=input()
num=list(number.strip())
n=len(num)
min_num=min(num)
for i in range(m):
    for j in range(n-1):
        if num[j+1]>num[j]:
            del num[j]
            break
print ''.join(num)
