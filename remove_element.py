class Solution():
    def removeElement(nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        numbers = 0
        if nums == []:
            return numbers
        for i in range(len(nums)):
            if nums[i] != val:
                nums[numbers] = nums[i]
                numbers += 1
        return numbers

    if __name__ == "__main__":
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        val = 2
        print removeElement(nums,val)