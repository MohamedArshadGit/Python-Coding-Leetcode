class Solution:
    def productExceptSelf(self,nums):
        output=[1]*len(nums)
        prefix=1
        for i in range(len(nums)):
            output[i]=prefix
            prefix=prefix*nums[i]
        postfix=1
        for i in range(len(nums)-1,-1,-1):
            output[i]=output[i]*postfix #y we are * with output[i] unlike just initializing like prefix
            # because if we did not pass values in output to postfix ,nums[i] will get resetted and
            # finally it will calculate only postfix so we are doing  output[i]=output[i]*postfix
            postfix=postfix*nums[i]
        return output
nums = [1,2,3,4]
nums1 = [-1,1,0,-3,3]
soln=Solution()
print(soln.productExceptSelf(nums))
print(soln.productExceptSelf(nums1))