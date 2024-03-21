yue=list(raw_input().strip())
hei=list(raw_input().strip())
n=len(hei)
m=0
for i in range(n):
    if yue[i].isalpha() or yue[i].isdigit():
        yue[i]='1'
    else:
        yue[i]='0'
    if yue[i]==hei[i]:
        m+=1
print str('%.2f' % (m/(n+0.0)*100))+'%'
