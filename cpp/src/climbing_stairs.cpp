/**
 * https://leetcode.cn/problems/min-cost-climbing-stairs/description/
 * 跳到第i个台阶，有两个方法：从i-1跳1级，从i-2跳2级，因此跳到i的最小cost为min{mincost(i-1) + cost(i-1),mincost(i-2)+cost(i-2)}
 * 最后跳完所有n个台阶，要么从n-1跳1级，要么从n-2跳2级，也就是代价为min{mincost(n-1) + cost(n-1),mincost(n-2)+cost(n-2)}
 * 因此这是个递归问题，从前往后递归计算
 */

#include <iostream>
#include <vector>

using namespace  std;

class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int size = cost.size();
        //跳到每一步楼梯的最小cost向量，增加了最后一步到达层
        vector<int> minCost(size + 1);
        //第一级和第二级楼梯可以直接到达
        minCost[0] = 0;
        minCost[1] = 0;

        for(int i = 2; i < size + 1; i++){
            minCost[i] = min(minCost[i-2] + cost[i-2], minCost[i-1] + cost[i-1]);
        }
//        for(int cost_item :minCost){
//            cout << cost_item << endl;
//        }
        return minCost[size];
    }
};

int main(){
    Solution solution;
    std::vector<int> cost = {1,100,1,1,1,100,1,1,100,1};
    cout << solution.minCostClimbingStairs(cost) << endl;
    return 0;
}