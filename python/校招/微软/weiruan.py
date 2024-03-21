N=input()
char=raw_input()
M=input()
ill_list=[]
count=0
for i in range(M):
    ill=raw_input()
    ill_list.append(ill)
    ill_list.append(ill[::-1])
def contain(char,ill_list):
    for s in ill_list:
        if s in char:
            return 1
    return 0
def f(char,ill_list):
    if contain(char,ill_list)==1:
        subchar=[]
        for i in range(len(char)):
            c=char[:i]+char[i+1:]
            subchar.append(c)
        sub_f=[f(x,ill_list)+1 for x in subchar]
        return min(sub_f)
    else:
        return 0
if N<10:
    print f(char,ill_list)
else:
    print 0
