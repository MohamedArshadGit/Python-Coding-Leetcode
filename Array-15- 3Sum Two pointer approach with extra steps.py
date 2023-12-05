class Solution:
    def threeSum(self,nums):
        res=[]
        nums.sort()
        for i,a in enumerate(nums):
            if i>0 and a==nums[i-1]:#to skip the dupliacte a once sorted bcos if we didnt skip it will return the duplicate answer
                continue
            l=i+1 #left pointer
            r=len(nums)-1 #right pointer
            while l<r:
                threesum=a+nums[l]+nums[r]
                if threesum>0:
                    r-=1
                elif threesum<0:
                    l+=1
                else:#means sums to zero
                    res.append([a,nums[l],nums[r]])# note append will work for multiple values insdide the list but not without list
                    l+=1 #to update left and right pointer because if duplicates we there it will return same results
                    # so do this,but we can do either left or right to be updated because in line 12 and 14 it will
                    # take care of either one so we just have to update either left or right here we update left
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        return res

nums = [-1, 0, 1, 2, -1, -4]
nums1 = [0,1,1]
nums2 = [0,0,0]

soln=Solution()
print(soln.threeSum(nums))
print(soln.threeSum(nums1))
print(soln.threeSum(nums2))