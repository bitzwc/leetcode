class Solution:
    @staticmethod
    def lengthOfLongestSubstring(s):
        """
        :type s: str
        :rtype: int
        """
        str_dist = {}
        result = 0
        j = 0
        for i in range(len(s)):
            if s[i] in str_dist.keys():
                j += 1
                result = len(str_dist.keys())
                str_dist = {}
            else:
                str_dist[s[i]] = i
        return result

    if __name__ == "__main__":
        s = "abcdddss"
        print lengthOfLongestSubstring(s)
        print list()