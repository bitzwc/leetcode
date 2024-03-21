n=input()
person=0
pmax=person
for i in range(n):
    line=raw_input()
    seg=line.strip().split(' ')
    up=int(seg[1])
    down=int(seg[0])
    person=person-down+up
    if person>pmax:
        pmax=person
print pmax
