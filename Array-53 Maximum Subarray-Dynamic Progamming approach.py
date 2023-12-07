'''53. Maximum Subarray
Medium
Topics
Companies

Given an integer array nums, find the
subarray
with the largest sum, and return its sum.



Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.



Constraints:

    1 <= nums.length <= 105
    -104 <= nums[i] <= 104



Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
Seen this question in a real interview before?
1/4
Yes
No
Accepted
3.5M
Submissions
7M
Acceptance Rate
50.5%
Topics
Array
Divide and Conquer
Dynamic Programming'''

#DYNMAIC PROGRAMMING APPROACH
class Solution:
    def maxSubArray(self,nums):
        currSum=0
        max_sub=nums[0] #just for sake initializing 1st number as subarray
        for n in nums:
            if currSum<0:
                currSum=0 #resetting if result from 2nd iteration ,if it is negative
            currSum=currSum+n #creating subarray
            max_sub=max(max_sub,currSum) #finding maximum subarray sum
        return max_sub

nums = [-2,1,-3,4,-1,2,1,-5,4]
nums1 = [1]
nums2=[5,4,-1,7,8]

soln=Solution()
print(soln.maxSubArray(nums))
print(soln.maxSubArray(nums1))
print(soln.maxSubArray(nums2))