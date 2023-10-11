'''209. Minimum Size Subarray Sum
Medium

Given an array of positive integers nums and a positive integer target, return the minimal length of a
subarray
whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

Constraints:

    1 <= target <= 109
    1 <= nums.length <= 105
    1 <= nums[i] <= 104
'''

def minSubArrayLen(target,nums):
    l=0 #initialize left pointer
    total=0
    res =float("inf") #this is infinity ,to set a number as infinity we use this
    subarray=[] #for my purpose to see which subarray is the least i used this empty sub array
    for r in range(len(nums)): # r in for loop is right pointer iterating through each number
        total=total+nums[r] #we start from left only but we dont consider left pointer because loop running from start only so no issue
        while total>=target: #use while instead of if, bcos in final it is not considering minimum subarray,also while loop run only once because we write a code inside while loop which reduces total in 3rd line
            res=min((r-l)+1,res) #this is for from which left pointer to right pointer nos the target has been acheived
            subarray=nums[l:r+1] #for personal to visualize which subarray is moving and adding up
            total=total-nums[l] #to move to 2nd number we minus the 1st value from total
            l+=1 #move the left pointer
    print(subarray)
    return 0 if res==float("inf") else res

target = 7
nums = [2,3,1,2,4,3]
a=minSubArrayLen(target,nums)
print(a)
print()
target = 4
nums = [1,4,4]
a=minSubArrayLen(target,nums)
print(a)
print()
target = 11
nums = [1,1,1,1,1,1,1,1]
a=minSubArrayLen(target,nums)
print(a)