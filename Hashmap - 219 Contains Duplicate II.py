'''
219. Contains Duplicate II
Solved
Easy
Topics
Companies

Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false



Constraints:

    1 <= nums.length <= 105
    -109 <= nums[i] <= 109
    0 <= k <= 105

Seen this question in a real interview before?
1/4
Yes
No
Accepted
825.8K
Submissions
1.9M
Acceptance Rate
44.2%
Topics
Array
Hash Table
Sliding Window
'''
'''THIS CODE IS TRICkY NOTE IT CAREFULLY'''
#Neetcode Method-sliding window
def containsnearbyduplicates(nums,k):
    window=set() #using set to store only unique values
    l=0
    for r in range(len(nums)):#(here we didnt start r from 1 bcos we need to add oth index value also to window set
        if (r-l)>k: #(in sum they said i-j should be less than k) so we use this ,also we need to remove left pointer value and increment to next pointer+9699999999999999
            window.remove(nums[l])
            l+=1
        if nums[r] in window: # Y we didnt check for r-l<=k bcos on 1st line in loop itself we check so not neededif duplicate values comes again we will return true
            return True
        else:
            window.add(nums[r]) #or we will add that number to window set
    return False

nums = [1,2,3,1]
k = 3
a=containsnearbyduplicates(nums,k)
print(a)

nums = [1,0,1,1]
k = 1
a=containsnearbyduplicates(nums,k)
print(a)

nums = [1,2,3,1,2,3]
k = 2
a=containsnearbyduplicates(nums,k)
print(a)

#my own method-Brute force but not passing test only 20 is passed out of 80 in neetcode
def containsNearbyDuplicate(nums,k):
    l=0
    for r in range(1,len(nums)):
        while l<r and r<len(nums):
            if nums[l]!=nums[r]:
                r+=1
                continue
            if nums[l]==nums[r] and (r-l)<=k:
                return True
            else:
                break
        l+=1
    return False

nums = [1,2,3,1]
k = 3
a=containsNearbyDuplicate(nums,k)
print(a)

nums = [1,0,1,1]
k = 1
a=containsNearbyDuplicate(nums,k)
print(a)

nums = [1,2,3,1,2,3]
k = 2
a=containsNearbyDuplicate(nums,k)
print(a)
print()

