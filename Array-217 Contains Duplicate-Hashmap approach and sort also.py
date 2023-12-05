#most efficient solution using hashmap
class Solution:
    def containsDuplicate(self,nums):
        hashset=set()
        for i in nums:
            if i in hashset: #checking if is in hashset
                return True
            hashset.add(i) #if not add it in our hashset
        return False
nums = [1, 2, 3, 1]
nums1 = [1,2,3,4]
nums2 = [1,1,1,3,3,4,3,2,4,2]
soln=Solution()
print(soln.containsDuplicate(nums))
print(soln.containsDuplicate(nums1))
print(soln.containsDuplicate(nums2))
print()
print()
#sort method using Two pointer
class Solution:
    def containsDuplicate(self,nums):
        l=0
        r=1
        nums.sort()
        while l<r and r<len(nums):
            if nums[l]==nums[r]:
                return True
            l+=1
            r+=1
        return False
sol=Solution()
print(sol.containsDuplicate(nums))
print(sol.containsDuplicate(nums1))
print(sol.containsDuplicate(nums2))
print()
#for loop
class Solution:
    def containsDuplicate(self,nums):
        l=0
        r=1
        nums.sort()
        for i in range(len(nums)):
            if r<len(nums) and nums[l]==nums[r]:
                return True
        return False
soli=Solution()
print(soli.containsDuplicate(nums))
print(soli.containsDuplicate(nums1))
print(soli.containsDuplicate(nums2))