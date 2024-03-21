from math import sqrt
coords=[]
for i in range(3):
    line=raw_input()
    seg=line.strip().split(' ')
    x,y,r=seg[0],seg[1],seg[2]
    coords.append((float(x),float(y),float(r)))
x1=coords[0][0]
y1=coords[0][1]
r1=coords[0][2]
x2=coords[1][0]
y2=coords[1][1]
r2=coords[1][2]
x3=coords[2][0]
y3=coords[2][1]
r3=coords[2][2]
x_temp=0
y_temp=0
r_temp=0

if r1==r2 and r1==r3:
    if x1==x2:
        x_temp,y_temp,r_temp=x1,y1,r1
        x1,y1,r1=x3,y3,r3
        x3,y3,r3=x_temp,y_temp,r_temp
    a=2*(y2*x1-y2*x3+y1*x3-y3*x1+y3*x2-y1*x2)
    b=(x1**2+y1**2)*(x3-x2)+(x2**2+y2**2)*(x1-x3)+(x3**2+y3**2)*(x2-x1)
    y=b/a
    c=y1**2-y2**2+x1**2-x2**2
    x=(y2-y1)/(x1-x2)*y+c/(2*(x1-x2))
    print x,y
else:
    if r1==r2 and r1!=r3:
        x_temp,y_temp,r_temp=x1,y1,r1
        x1,y1,r1=x3,y3,r3
        x3,y3,r3=x_temp,y_temp,r_temp
    if r1!=r2 and r1==r3:
        x_temp,y_temp,r_temp=x1,y1,r1
        x1,y1,r1=x2,y2,r2
        x2,y2,r2=x_temp,y_temp,r_temp
    a=(pow(r2,2)*x1-pow(r1,2)*x2)/(pow(r1,2)-pow(r2,2))
    b=(pow(r2,2)*y1-pow(r1,2)*y2)/(pow(r1,2)-pow(r2,2))
    c=pow(r1,2)*pow(r2,2)*(pow(x1-x2,2)-pow(y1-y2,2))/pow(pow(r1,2)-pow(r2,2),2)
    d=(pow(r3,2)*x1-pow(r1,2)*x3)/(pow(r1,2)-pow(r3,2))
    e=(pow(r3,2)*y1-pow(r1,2)*y3)/(r1**2-r3**2)
    f=pow(r1,2)*pow(r3,2)*(pow(x1-x3,2)-pow(y1-y3,2))/pow(pow(r1,2)-pow(r3,2),2)
    g=pow(d-a,2)+pow(b,2)-e**2+c-f
    A=4*(pow(b-e,2)-pow(d-a,2))
    B=4*g*(b-e)-8*b*(d-a)**2
    C=g**2-4*(d-a)**2*(b**2+c)
    delta=sqrt(B**2-4*A*C)
    y_1=(-B+delta)/(2*A)
    if y_1<=1000:
        x_1=-a+sqrt((y_1+b)**2+c)
        if x_1>-1000:
            print x_1,y_1
        x_2=-a-sqrt((y_1+b)**2+c)
        if x_2>-1000:
            print x_2,y_1
    y_2=(-B-delta)/(2*A)
    if y_2<=1000:
        x_3=-a+sqrt((y_2+b)**2+c)
        if x_3>-1000:
            print x_3,y_2
        x_4=-a-sqrt((y_2+b)**2+c)
        if x_4>-1000:
            print x_4,y_2
