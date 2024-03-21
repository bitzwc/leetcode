class Solution():
    def twoSum(self, nums, a):
        ret = []
        for i,b in enumerate(nums):
            for j,c in enumerate(nums[i+1:]):
                if b+c==-a:
                    ret.append([a,b,c])
        return ret

    def threeSum(self,nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for i,a in enumerate(nums):
            result.append(twoSum(self, nums[i:], a))
        return list(result)



    if __name__ == "__main__":
        nums = [-1, 0, 1, 2, -1, -4]

        print nums
