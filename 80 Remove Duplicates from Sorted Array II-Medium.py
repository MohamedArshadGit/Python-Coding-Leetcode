def removeDuplicates(nums):
    l=0#initialise left and right pointer
    r=0
    while r<len(nums):
        count=1 #atleast 1 number will be there if u put zero it take less count eg if three 1 are there it will take as 2 if u put as 0 so put 2
        while (r+1)<len(nums) and nums[r]==nums[r+1]:#checking for equal
            r+=1 #moving right pointer till numbers are equal
            count+=1 #eg counting how many 1's are there
        for i in range(min(2,count)):#we need atmost 2 duplicate nos so put min(2,count may be 1 or 2 or 3 but we need acc to no of repitations so put like this)
            nums[l]=nums[r] #now update till right pointer
            l+=1 #update left pointer to put number to next position
        r+=1
    return nums,l


nums = [1,1,1,2,2,3]
a=removeDuplicates(nums)
print(a)
nums = [0,0,1,1,1,1,2,3,3]
a=removeDuplicates(nums)
print(a)