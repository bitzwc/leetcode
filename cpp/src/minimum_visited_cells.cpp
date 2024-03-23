//
// Created by zhangwencheng on 2024/3/22.
// https://leetcode.cn/problems/minimum-number-of-visited-cells-in-a-grid/?envType=daily-question&envId=2024-03-22
// 起点固定，终点固定
// 转移方式有2种：向右移动、向下移动，移动步数<=为当前格子的数字
// BFS
//
#include <vector>
#include <queue>
#include <iostream>

using namespace std;

class Solution {
public:
    int minimumVisitedCells(vector<vector<int>>& grid) {
        //横坐标，纵坐标，值，第几个格子
        queue<tuple<int, int, int, int>> queue1 = {};
        queue1.emplace(0, 0, grid[0][0], 1);

        //行数
        int m = grid.size();
        //列数
        int n = grid[0].size();
//        cout << m << " " << n << endl;

        // 记录是否已经进入过队列
        vector<vector<bool>> vis(m, vector<bool>(n, false));
        vis[0][0] = true;

        while(!queue1.empty()){
            auto node = queue1.front();
            int i = get<0>(node);
            int j = get<1>(node);
            int step = get<2>(node);
            int level = get<3>(node);
            //当前所在点是否终点
            if(i == m-1 && j == n-1){
                return level;
            }
            cout << i << " " << j << " " << endl;
            queue1.pop();
            //向右移动，在step步内移动
            //这里存在重复访问节点的情况，已经访问过的节点，没必要进循环，可以继续优化时间复杂度
            for(int k=j+1; k<=n-1 && k<=j+step; k++){
                cout << i << " " << k << endl;
                //是否到达终点
                if(i == m-1 && k == n-1){
                    return level + 1;
                }
                if(grid[i][k] != 0 && !vis[i][k]) {
                    queue1.emplace(i, k, grid[i][k], level + 1);
                    vis[i][k] = true;
                }
            }
            //向下移动
            for(int k=i+1; k<=m-1 && k<=i+step; k++) {
                //是否到达终点
                if (k == m - 1 && j == n - 1) {
                    return level + 1;
                }
                if(grid[k][j] != 0 && !vis[k][j]){
                    queue1.emplace(k, j, grid[k][j], level + 1);
                    vis[k][j] = true;
                }
            }
        }
        return -1;
    }
};


int main(){
    vector<vector<int>> grid1 = {{3,4,2,1},{4,2,3,1},{2,1,0,0},{2,4,0,0}};
    vector<vector<int>> grid2 = {{3,4,2,1},{4,2,1,1},{2,1,1,0},{3,4,1,0}};
    vector<vector<int>> grid3 = {{2,1,0},{1,0,0}};
    vector<vector<int>> grid4 = {{9,8,7,6,5,4,3,2,1,1,0}};
    Solution solution;
    cout << solution.minimumVisitedCells(grid4) << endl;
    return 0;
}