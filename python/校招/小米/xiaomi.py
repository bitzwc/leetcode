n=input()
length=[0]*n
maxlen=0
for i in range(n-1):
    fuzi=raw_input()
    fuzi=fuzi.strip().split(' ')
    fu=int(fuzi[0])
    zi=int(fuzi[1])
    length[zi]=length[fu]+1
    if length[zi]>maxlen:
        maxlen=length[zi]
print maxlen+1
    
