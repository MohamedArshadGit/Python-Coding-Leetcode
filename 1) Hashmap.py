def twosum(nums,target):
    prevmap ={}
    
    for i ,n in enumerate(nums):
        diff =target-n
        if diff in prevmap:
            return prevmap[diff],i

        else:
            prevmap[n]=i
            print(prevmap)
            #print(prevmap[n],"::",i)
    


nums = [2,7,11,15]
target = 9

nums1 = [3,2,4]
target1 = 6

nums2 = [3,3]
target2 = 6

ans = twosum(nums1,target1)
print(ans)