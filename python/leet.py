class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n=len(height)
        maxwater=0
        for i in range(n):
            for j in range(i+1,n):
                if min(height[j],height[i])*(j-i)>maxwater:
                    maxwater=min(height[j],height[i])*(j-i)
        return maxwater
s=Solution()
print s.maxArea([1,1])