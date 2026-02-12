def move_zero(nums):
    l=0
    for r in range(len(nums)):
        if nums[r] !=0:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
    return nums


nums = [0,0,1,0,3,12]
# Output: [1,3,12,0,0]

a=move_zero(nums)
print(a)