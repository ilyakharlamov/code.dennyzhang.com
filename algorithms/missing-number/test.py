#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Description:
##     https://leetcode.com/problems/missing-number/description/
## ,-----------
## | Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
## | 
## | For example,
## | Given nums = [0, 1, 3] return 2.
## | 
## | Note:
## | Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
## `-----------
## 
## Tags:
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-25 17:06:36>
##-------------------------------------------------------------------
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ## Idea: caculated the desired sum. Then add up all the numbers. Do the substraction.
        ## Complexity: Time O(n), Space O(1)
        n = len(nums)
        supposed_sum = (n * (n+1))/2
        for i in range(0, n):
            supposed_sum -= nums[i]
        return supposed_sum
