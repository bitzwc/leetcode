st1=raw_input()
n=int(st1.split(" ")[0])
m=int(st1.split(" ")[1])
list=[]
for t in range(m):
    l=raw_input()
    list.append(l)
maxmax=0
fix=0
d={}
for t in range(len(list)):
    day1=int(list[t].split(" ")[0])
    high1=int(list[t].split(" ")[1])
    d[day1]=high1
d=sorted(d.iteritems(),key=lambda t:t[0],reverse=False)
list=[]
for t in range(len(d)):
    list.append(str(d[t][0])+" "+str(d[t][1]))
for t in range(len(list)-1):
    day1=int(list[t].split(" ")[0])
    day2=int(list[t+1].split(" ")[0])
    high1=int(list[t].split(" ")[1])
    high2=int(list[t+1].split(" ")[1])
    maxlinshi=0
    daycha=day2-day1
    if high2>=high1:
        highcha=high2-high1
    else:
        highcha=high1-high2
    duochu=(daycha-highcha)/2
    if daycha-highcha<0:
        print "IMPOSSIBLE"
        fix=1
    else:
        maxlinshi=duochu+max(high1,high2)
        if maxlinshi>maxmax:
            maxmax=maxlinshi
if fix==0:
    day1=int(list[0].split(" ")[0])
    high1=int(list[0].split(" ")[1])
    max1=high1+day1-1
    daymo=int(list[-1].split(" ")[0])
    highmo=int(list[-1].split(" ")[1])
    max2=highmo+n-daymo
    if max(max1,max2)>maxmax:
        maxmax=max(max1,max2)
    print maxmax
