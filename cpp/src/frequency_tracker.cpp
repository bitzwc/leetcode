//
// Created by zhangwencheng on 2024/3/21.
// https://leetcode.cn/problems/frequency-tracker/?envType=daily-question&envId=2024-03-21
// 对象的初始化、元素统计（map）、查询
//
#include "iostream"
#include "map"
using namespace std;

class FrequencyTracker {
public:
    //数字的出现次数map
    map<int, int> nums_map;
    //出现次数的数字个数map
    map<int, int> nums_fre_map;

    FrequencyTracker() {

    }

    void add(int number) {
        //先去掉1个有这么多number的
        --nums_fre_map[nums_map[number]];
        //先在number_map里加上1个，再在nums_fre_map增加一个对应number的计数
        ++nums_fre_map[++nums_map[number]];
    }

    void deleteOne(int number) {
        if(nums_map[number]){
            //先去掉1个有这么多number的
            --nums_fre_map[nums_map[number]];
            //先在number_map里加上1个，再在nums_fre_map增加一个对应number的计数
            ++nums_fre_map[--nums_map[number]];
        }
    }

    bool hasFrequency(int frequency) {
        //这里for循环每次都需要遍历，时间复杂度太高
        if(nums_fre_map[frequency] > 0){
            return true;
        }
        return false;
    }
};

/**
 * Your FrequencyTracker object will be instantiated and called as such:
 * FrequencyTracker* obj = new FrequencyTracker();
 * obj->add(number);
 * obj->deleteOne(number);
 * bool param_3 = obj->hasFrequency(frequency);
 */
int main(){
    FrequencyTracker frequencyTracker;
    frequencyTracker.add(3);
    frequencyTracker.add(3);
    frequencyTracker.deleteOne(3);
    std::cout << frequencyTracker.hasFrequency(1);
    return 0;
}