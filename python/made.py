def foo(output, open, close, pairs):
    if open == pairs and close == pairs:
        print output
    else:
        if open<pairs:
            foo(output+'(', open+1, close, pairs)
        if close<open:
            foo(output+')', open, close+1, pairs)
while 1:
    n=input()
    foo('',0,0,n)
