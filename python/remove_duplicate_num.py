class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numbers = 0
        for i in range(len(nums)):
            item = nums[i]
            if item != nums[numbers]:
                numbers += 1
                nums[numbers] = item
        return numbers + 1
