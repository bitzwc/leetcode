import numpy as np
para=raw_input()
seg1=para.strip().split(' ')
k=seg1[0]
m=seg1[1]
n=seg1[2]
arr=raw_input()
A=np.reshape(arr.strip().split(' '),(m,n))
arr=raw_input()
h=np.reshape(arr.strip().split(' '),(k,k))
B=np.array(0,(k,k))
print A,h,B
