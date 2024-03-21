def findCrossMaxSum(List, left, mid, right):
    left_sum=-10000
    sum=0
    for i in range(mid, left-1, -1):
        sum += List[i]
        if sum>left_sum:
            left_sum = sum
            max_left = i
    right_sum=-10000
    sum = 0
    for j in range(mid+1, right+1):
        sum += List[j]
        if sum > right_sum:
            right_sum=sum
            max_right=j
    return max_left, max_right, left_sum+right_sum
def findMaxSum(List, left, right):
    if left == right:
        return left, right, List[left]
    else:
        mid = (left + right)/2
        left_low, left_high, left_sum = findMaxSum(List, left, mid )
        right_low, right_high, right_sum = findMaxSum(List, mid+1, right)
        cross_low, cross_high, cross_sum = findCrossMaxSum(List, left, mid, right)
        if left_sum > right_sum and left_sum>cross_sum:
            return left_low,left_high,left_sum
        elif right_sum>left_sum and right_sum >cross_sum:
            return right_low,right_high,right_sum
        else:
            return cross_low,cross_high,cross_sum
print(findMaxSum([-1,3,-2,4,-2,3,-8,9],0,7))