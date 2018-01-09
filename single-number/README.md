# Puzzle: Single Number     :BLOG:Numbers:


---

Identity number which appears exactly once.  

---

Given an array of integers, every element appears twice except for one. Find that single one.  

Note:  
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?  

Hint: Time O(n), Space O(1)  

<https://leetcode.com/problems/single-number/description/>  

    class Solution(object):
        def singleNumber(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            x = 0
            for i in nums:
                x = x ^ i
            return x
    
    if __name__ == '__main__':
        s = Solution()
        print s.singleNumber([1, 2, 1])
        print s.singleNumber([2, 2, 1])

Leave me comments, if you know how to solve.  

More Reading:  
-   [Puzzle: Puzzle: Single Number II](http://brain.dennyzhang.com/single-number-ii/)
-   [Puzzle: Find the Duplicate Number](http://brain.dennyzhang.com/find-duplicate-num/)
-   [Puzzle: Find All Numbers Disappeared in an Array](http://brain.dennyzhang.com/find-disappeared/)