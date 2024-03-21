class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        A.sort()
        B.sort()
        C.sort()
        D.sort()
        result = []
        dist1 = {}
        dist2 = {}
        for i in range(len(A)):
            for j in range(len(B)):
                s = A[i]+B[j]
                if s in dist1:
                    value = dist1[s]
                    value.append([i,j])
                else:
                    value = [[i,j]]
                dist1[s]=value
        print dist1
        for i in range(len(C)):
            for j in range(len(D)):
                s = C[i]+D[j]
                if s in dist2:
                    value = dist2[s]
                    value.append([i,j])
                else:
                    value = [[i,j]]
                dist2[s]=value
        for s in dist1:
            if -s in dist2:
                lst1 = dist1[s]
                lst2 = dist2[-s]
                print lst1
                print lst2
                for l1 in lst1:
                    for l2 in lst2:
                        lst = l1+l2
                        result.append(lst)
        return len(result)

if __name__ == "__main__":
    A = [-1, -1]
    B = [-1, 1]
    C = [-1, 1]
    D = [1, -1]
    print Solution().fourSumCount(A,B,C,D)