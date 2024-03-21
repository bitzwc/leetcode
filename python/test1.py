# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, array, target):
        # write code here
        all_num=[]
        for arr in array:
            all_num=all_num+arr
        if target in all_num:
            print all_num,target
            print "true"
        else:
            print all_num,target
            print "false"
