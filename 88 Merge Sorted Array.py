def merge(nums1,nums2,m,n):
    last=m+n-1
    while m>0 and n>0:
        if nums1[m-1]>nums2[n-1]:
            nums1[last]=nums1[m-1]
            m=m-1
        else:
            nums1[last]=nums2[n-1]
            n=n-1
        last=last-1
    while n>0:
        nums1[last]=nums2[n-1]
        n=n-1
        last=last-1
    print(nums1)



nums1=[1,2,3,0,0,0]
nums2=[2,5,6]
m=3
n=3
a=merge(nums1,nums2,m,n)
print(a)