def removeelement(nums:list[int],val:int)-> int:
    l=0
    for i in range(len(nums)):
        if nums[i]!=val:
            nums[l]=nums[i]
            l+=1
    return l,nums

nums = [3,2,2,3]
val = 3

ans =removeelement(nums,val)
print(ans)