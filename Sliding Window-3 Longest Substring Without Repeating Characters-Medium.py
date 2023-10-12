def lengthoflongestsubstring(s):
    l=0
    charset=set() #to have only unique values and no duplliactes inside it
    res=0
    current_len=0
    for r in range(len(s)):
        while s[r] in charset:
            charset.remove(s[l]) #this if for to remove the 1st duplicate value
            l+=1
        charset.add(s[r]) #this is like 1st step adding unique values in charset
        res=max(r-l+1,res)

    return res

s = "abcabcbb"
a=lengthoflongestsubstring(s)
print(a)
s = "bbbbb"
a=lengthoflongestsubstring(s)
print(a)
s = "pwwkew"
a=lengthoflongestsubstring(s)
print(a)