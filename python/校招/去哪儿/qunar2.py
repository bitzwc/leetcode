while 1:
    s=raw_input()
    str1,str2=s.strip().split(' ')
    a=len(list(str1))
    b=len(list(str2))
    c=len(set(str1+str2))
    if c==a+b:
        print 'false'
    else:
        print 'true'
