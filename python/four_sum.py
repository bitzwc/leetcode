class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        sum_dist = {}
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                sum = nums[i] + nums[j]
                if sum in sum_dist:
                    lst = sum_dist[sum]
                    lst.append([i, j])
                else:
                    lst = [[i, j]]
                sum_dist[sum] = lst
        for sum in sum_dist:
            if target - sum in sum_dist:
                lst1 = sum_dist[sum]
                lst2 = sum_dist[target - sum]
                for l1 in lst1:
                    for l2 in lst2:
                        l = l1 + l2
                        if len(set(l)) == len(l):
                            l.sort()
                            item = [nums[index] for index in l]
                            if item not in result:
                                result.append(item)
        return result
