class Solution:
    def maxProduct(self,nums):
        max_num,min_num=1,1
        res=max(nums)#y we are using max(nums) instead of 0 bcos eg if we have array with only 1 number [-1] -1 have to be the max number so we use max for safer side
        for n in nums:
            #if n == 0:
               # max_num, min_num = 1, 1(not needed becos we are using n as 3rd variable in max_num and min_num
            # that will handle)
            temp_max=max_num*n#y we are calculating temp_max bcos in min_num variable
            # while calculating max_num it will get updated by previous line so we storing max_num in temp variable
            # and use it in min_num
            max_num=max(max_num*n,min_num*n,n) #y using 3rd variable n bcos if array is like
            # [-1,8,2] in 1st iteration maxnum and minnum is -1 in 2nd iteration will become as -8
            # but 8*2=16 is the answer
            #so if we adding n in 3rd variable will give in 1st iteration -1 in 2nd iteration it
            # will take 8 so answer will come properly
            min_num=min(temp_max,min_num*n,n)
            res=max(res,max_num)
        return res


nums = [2, 3, -2, 4]
nums1=[-2,0,-1]
soln=Solution()
print(soln.maxProduct(nums))
print(soln.maxProduct(nums1))

