'''1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:

    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?'''

#My own Method
def twoSum(nums, target):
        l=0
        output=[]
        for r in range(1,len(nums)):
            while l<r and r<len(nums):
                number=nums[l]+nums[r]
                if number==target:
                    output.extend([l,r]) #append can be used only with 1 number for 2 number we need to
                    # put append([0,1]) output is [[0,1]] leetcode doesnt accept multiple lists ie list inside a list
                    #so use EXTEND if we use extend([0,1]) output will be single list [0,1]
                    return output
                else:
                    r+=1
            l+=1

nums = [2,7,11,15]
target = 9
a=twoSum(nums,target)
print(a)

nums = [3,2,4]
target = 6
a=twoSum(nums,target)
print(a)

nums = [3,3]
target = 6
a=twoSum(nums,target)
print(a)

nums=[3,2,3]
target=6
a=twoSum(nums,target)
print(a)
print()

##Neetcode efficient solution
def twosum(nums,target):
    prev_hash={}
    for i,n in enumerate(nums):
        diff=target-n
        if diff in prev_hash:
            return [prev_hash[diff],i]
        else:
            prev_hash[n]=i
nums=[3,2,3]
target=6
a=twosum(nums,target)
print(a)