//
// Created by zhangwencheng on 2024/3/23.
// https://leetcode.cn/problems/count-distinct-numbers-on-board/?envType=daily-question&envId=2024-03-23
// bfs粗暴解法：对小于n的数遍历，求得结果后，加入队列，继续遍历
// 简单解法：对于任意n>=3，都满足n对n-1求余，结果为1，因此n-1一定是该题的一个解，往前递推，可知2到n-1都是解，因此解的个数为n-1和1的较大值
//
#include <algorithm>
#include "iostream"

using namespace std;
class Solution {
public:
    int distinctIntegers(int n) {
        return max(n - 1, 1);
    }
};

int main(){
    Solution solution;
    std::cout << solution.distinctIntegers(1);
    return 0;
}