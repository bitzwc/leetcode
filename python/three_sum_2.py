class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        sum_dist = {}
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                sum = nums[i] + nums[j]
                if sum in sum_dist:
                    lst = sum_dist[sum]
                    lst.append([i,j])
                else:
                    lst = [[i,j]]
                sum_dist[sum] = lst
        for i in range(len(nums)):
            if -nums[i] in sum_dist:
                lst = sum_dist[-nums[i]]
                for l in lst:
                    if i not in l:
                        r = l + [i]
                        r.sort()
                        num = [nums[index] for index in r]
                        if num not in result:
                            result.append(num)
        return result
if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4]
    print Solution().threeSum(nums)