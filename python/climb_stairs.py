class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<1:
            return 0
        Solution.stairs = [1,2]
        Solution.result = []
        self.DFS(n, 0, [])
        return len(Solution.result)
    def DFS(self, target, i, lst):
        if target == 0 and lst not in Solution.result:
            Solution.result.append(lst)
        if target-1>=0:
            self.DFS(target-1, 0, lst+[1])
        if target-2>=0:
            self.DFS(target-2, 0, lst+[2])

if __name__ == "__main__":
    print(Solution().climbStairs(10))