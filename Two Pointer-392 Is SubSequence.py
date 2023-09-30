'''392. Is Subsequence

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false

Constraints:

    0 <= s.length <= 100
    0 <= t.length <= 104
    s and t consist only of lowercase English letters.
'''

def isSubsequence(s,t):
    i=0 #pointers for s
    j=0 #pointer for t to traverse through t string
    while i<len(s) and j<len(t):
        if s[i]==t[j]: #it compares s and t values through pointer if not found it will increment the j
            i+=1 #both s th and t th string are equal so increment i and j to compare for next letter
            j+=1

        else:
            j+=1 #s value not found in t so increment j
    return True if i==len(s) else False

s="abc"
t="ahbgdc"
ss = "axc"
tt = "ahbgdc"
a=isSubsequence(s,t)
print(a)