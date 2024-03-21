/*
 *  Created by zhangwencheng on 2024/3/21.
 *  https://leetcode.cn/problems/minimum-operations-to-convert-number/
 *  固定起点和终点，寻找最短路径BFS，用队列，不用递归
 *  每个节点是nums中元素和运算符的组合，比如nums有2个元素，则有2*3=6个子节点
 *  一旦节点值超过1000，则不能再参与计算
 *  如果遍历完成，都没有找到路径，则返回-1
 *  时间复杂度O(n)
 *  空间复杂度O(1)：队列、map，最多1000个
 */

#include <vector>
#include <iostream>
#include <queue>
#include <list>
#include <map>
using namespace std;

//提交leetcode解法类
class Solution {
public:
    int minimumOperations(vector<int>& nums, int start, int goal) {
        //要遍历的节点队列
        std::queue<pair<int, int>> queue;
        queue.emplace(start, 0);

        //已访问的节点，避免重复计算
        map<int, int> namemap;
        namemap[start] = 1;

        //3种操作符：+、-、^，函数lambda表达式
        std::function<int(int, int)> plus = [](int a, int b) { return a + b; };
        std::function<int(int, int)> minus = [](int a, int b) { return a - b; };
        std::function<int(int, int)> x_or = [](int a, int b) { return a ^ b; };
        vector<function<int(int, int)>> funcs = {plus, minus, x_or};

        //退出条件：队列里没有需要遍历的节点，复杂度1000
        while(!queue.empty()){
            //队列pop元素
            pair<int, int> node = queue.front();
            queue.pop();
            int num = node.first;
            int level = node.second;
//            cout << num << ", " << level << endl;
            //遍历nums，复杂度n
            for(int n: nums){
                //遍历操作符，将运算结果写入queue，复杂度3
                for(auto func: funcs) {

                    int next_num = func(num, n);
                    if(next_num == goal) {
                        return level + 1;
                    }
                    //判断该节点是否满足目标条件，0-1000范围内会出现多次，没有必要在最外层while循环，这里控制queue小于1000
                    if(next_num >= 0 && next_num <= 1000) {
//                        cout << next_num << endl;
                        //是否遍历过
                        if (namemap.find(next_num) == namemap.end()) {
                            namemap[next_num] = 1;
                            //将该节点的子节点添加到队列中
                            queue.emplace(next_num, level + 1);
                        }
                    }
                }
            }
        }
        return -1;
    }
};

int main(){
    vector<int> nums = {2,4,12}; //nums的元素不相等
    int start = 2;
    int goal = 12;
    Solution solution = Solution();
    int cnt = solution.minimumOperations(nums, start, goal);
    cout << cnt << endl;
    return 0;
}