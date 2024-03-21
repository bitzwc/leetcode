def findMaxSum(List):
    n=len(List)
    ThisSum=0
    MaxSum=0
    for i in range(n):
        ThisSum += int(List[i])
        if ThisSum>MaxSum:
            MaxSum =ThisSum
        elif ThisSum<0:
            ThisSum=0
    return MaxSum
