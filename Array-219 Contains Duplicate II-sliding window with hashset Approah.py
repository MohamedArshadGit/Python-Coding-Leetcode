'''219. Contains Duplicate II
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
807.6K
Submissions
1.8M
Acceptance Rate
44.0%
Topics
Array
Hash Table
Sliding Window'''

#read the question very properly and see the solution again in future
class Solution:
    def containsNearbyDuplicate(self,nums,k):
        windowset=set()
        l=0
        for r in range(len(nums)):
            if abs(l-r)>k:#abs means give only positive values still if the result is negative
                windowset.remove(nums[l])
                l+=1 #very important we should increment here
            if nums[r] in windowset:
                return True
            windowset.add(nums[r])
        return False

nums = [1,2,3,1]
k = 3
nums1 = [1,0,1,1]
k1 = 1
nums2 = [1,2,3,1,2,3]
k2 = 2
soln=Solution()
print(soln.containsNearbyDuplicate(nums,k))
print(soln.containsNearbyDuplicate(nums1,k1))
print(soln.containsNearbyDuplicate(nums2,k2))