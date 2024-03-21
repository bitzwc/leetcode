line=raw_input()
seg=line.strip().split(' ')
count=seg[0].strip('{}').split(',')
value=seg[1].strip('{}').split(',')
all_shibing=[]
for i in range(len(value)):
    all_shibing=all_shibing+[int(value[i])]*int(count[i])
print(all_shibing)
