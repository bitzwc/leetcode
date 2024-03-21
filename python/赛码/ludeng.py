line1=raw_input()
seg1=line1.strip().split(' ')
n=int(seg1[0])
l=int(seg1[1])
line2=raw_input()
seg2=line2.strip().split(' ')
deng=[int(s) for s in seg2]
deng.sort()
maxdiff=max(2*(deng[0]-0),2*(l-deng[-1]))
for i in range(n-1):
    diff=deng[i+1]-deng[i]
    if diff>maxdiff:
        maxdiff=diff
print "%.2f" %(maxdiff/2.0) 
