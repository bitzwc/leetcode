n=input()
line=raw_input().strip().split(' ')
numbers=[int(x) for x in line]
ji=ou=0
for i in numbers:
    if i%2==0:
        ou+=1
    else:
        ji+=1
print abs(ji-ou)