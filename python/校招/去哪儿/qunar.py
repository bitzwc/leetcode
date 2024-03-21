while 1:
    s=raw_input()
    str1,str2=s.strip().split(' ')
    str1=set(str1)
    str2=set(str2)
    if str1==str2:
        print 'true'
    else:
        print 'false'
