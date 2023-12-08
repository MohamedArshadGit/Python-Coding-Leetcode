'''45. Jump Game II
Solved
Medium
Topics
Companies

You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

    0 <= j <= nums[i] and
    i + j < n

Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].



Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: nums = [2,3,0,1,4]
Output: 2



Constraints:

    1 <= nums.length <= 104
    0 <= nums[i] <= 1000
    It's guaranteed that you can reach nums[n - 1].

Seen this question in a real interview before?
1/4
Yes
No
Accepted
1.1M
Submissions
2.7M
Acceptance Rate
40.2%
Topics
Array
Dynamic Programming
Greedy'''

class Solution:
    def jump(self,nums):
        output=0
        l=0
        r=0
        while r<len(nums)-1:
            farthest=0 #farthest will reset in each while loop
            for i in range(l,r+1):#y r+1 in python? only if we give r+1 it will work properly
                farthest=max(farthest,i+nums[i])
            l=r+1
            r=farthest #to make next left to right portion
            output+=1
        return output

nums = [2,3,1,1,4]
nums1 = [2, 3, 0, 1, 4]
soln=Solution()
print(soln.jump(nums))
print(soln.jump(nums1))
