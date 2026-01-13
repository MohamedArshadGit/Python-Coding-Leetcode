strs = ["flower","flow","flight"]
def longest_common_prefix(strs):
    res =''
    for i in range(0,len(strs[0])):
        for s in strs:
            if i==len(s) or s[i]!=strs[0][i]:
                return res
            
        res = res+s[i]
        # #or res =res +strs[0][i]

ans =longest_common_prefix(strs)
print(ans)
            
        
        
