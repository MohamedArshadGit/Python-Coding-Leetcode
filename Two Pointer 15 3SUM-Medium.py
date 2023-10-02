'''15. 3Sum
Medium

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
 such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
'''

def Threesum(nums): #To do this problem a+b+c for b+c we use 2 pointers and 2 sum for we use for loop
    res=[]
    nums.sort()#we need to sort to get the result
    print(nums)
    for i,a in enumerate(nums):
        if i>0 and a==nums[i-1]: #if a has duplicate in next loop it will skip eg here we have two -1 after sorting in next loop it will take -1 again and that should be done coz result will be same so skip it
            continue
        l=i+1 #2sum strategy left pointer and right pointer here b and c is l and r b should be next value of a so i+1
        r=len(nums)-1
        while l<r:
            threesum=a+nums[l]+nums[r]
            if threesum>0:
                r-=1
            elif threesum<0:
                l+=1
            else:
                res.append([a,nums[l],nums[r]])
                l+=1
                while nums[l]==nums[l-1] and l<r: #if duplicates in b and c we have to skip it so we shift left .....and right will taken care in top line >0 r-=1 so ignore right
                    l+=1
    return res
nums = [-1,0,1,2,-1,-4]
a=Threesum(nums)
print(a)