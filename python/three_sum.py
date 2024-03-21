class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for i in range(len(nums)-2):
            left = i + 1
            right = len(nums) - 1
            while left<right:
                sum = nums[left] + nums[i] + nums[right]
                if sum == 0:
                    lst = [nums[i], nums[left], nums[right]]
                    if lst not in result:
                        result.append(lst)
                    left, right = left + 1, right -1
                elif sum >0:
                    right -= 1
                elif sum<0:
                    left += 1
        return result

if __name__ == "__main__":
    nums = [3,0,-2,-1,1,2]
    print Solution().threeSum(nums)
