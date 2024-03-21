n=input()
lines=[]
for i in range(n):
    raw=raw_input()
    coords=raw.strip().split(' ')
    xi=int(coords[0])
    yi=int(coords[1])
    xj=int(coords[2])
    yj=int(coords[3])
    lines.append(((xi,yi),(xj,yj)))
#print lines
for i in range(n):
    for j in range(n):
        if j==i:
            continue
        else:
            line1=lines[i]
            line2=lines[j]
            if line1[0][0]==line2[0][0] and line1[0][1]==line2[0][1] and line1[1][0]!=line2[1][0] and line1[1][1]!=line2[1][1]:
                if (line2[1],(line1[1][1],line2[1][0])) in lines and (line1[1],(line1[1][1],line2[1][0])) in lines:
                    print ' '.join([str(line1[0][0]),str(line1[0][1]),str(line1[1][1]),str(line2[1][0])])
            
