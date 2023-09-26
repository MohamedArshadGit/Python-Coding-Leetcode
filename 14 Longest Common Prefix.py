'''14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.



Constraints:

    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lowercase English letters.

'''

def longestcommonprefix(str):
    res=''
    for i in range(len(strs[0])):
        for s in strs:
            print(i)
            print(s[i])
            print(strs[0][i])
            if i==len(s) or s[i]!=strs[0][i]: #note this i=len(s) see that later
                return res
        res=res+strs[0][i]
strs=["flower","flow","flight"]
a=longestcommonprefix(strs)
print(a)
