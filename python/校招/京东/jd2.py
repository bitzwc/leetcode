new=True
record={}
line=raw_input()
n=int(line.strip().split(' ')[0])
m=int(line.strip().split(' ')[1])
while new:
    print n,m
    line=raw_input()
    record[(n,m)]=[]
    i=0
    while line!='\n' and i<m: 
        record[(n,m)].append((line.strip().split(' ')[0],line.strip().split(' ')[1]))
        print record
        line=raw_input()
        i+=1
    if line=='\n':
        break
    else:
        n=int(line.strip().split(' ')[0])
        m=int(line.strip().split(' ')[1])
    
