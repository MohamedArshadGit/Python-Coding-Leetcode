'''5. Longest Palindromic Substring
Medium
Topics
Companies
Hint

Given a string s, return the longest
palindromic
substring
in s.



Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"



Constraints:

    1 <= s.length <= 1000
    s consist of only digits and English letters.

Seen this question in a real interview before?
1/4
Yes
No
Accepted
2.8M
Submissions
8.4M
Acceptance Rate
33.4%
Topics
String
Dynamic Programming'''

def longest_Palindrome(s): #410 ms speed
    res = ''
    reslen = 0


    # odd length expansion
    for i in range(len(s)):
        l, r = i, i #note i has been given to this very important due to tis only it is splitting from left to right
        while l >= 0 and r < len(s) and s[l] == s[r]: #edge case and to check when both the end words are same once after iteration
            if r - l + 1 > reslen: #to see which is the largest substring palindrome
                reslen=r-l+1
                res=s[l:r+1]
            l-=1
            r+=1
    #even length expansion
        l,r=i,i+1
        while l>=0 and r<len(s) and s[l]==s[r]:
            if r-l+1>reslen:
                reslen=r-l+1
                res=s[l:r+1]
            l-=1
            r+=1
    return res

s = "babad"
s1 = "cbbd"
print(longest_Palindrome(s))
print(longest_Palindrome(s1))
print()

#soln of leetcode plus completing in one function with chatgpt=>but time is 6904ms
class Solution:
    def longestPalindrome1(self, s):
        res = ''
        max_len = 0
        def sub(s,l,r):
            nonlocal res
            nonlocal max_len #The nonlocal max_len, res statement inside the sub function allows the sub function to access and modify the max_len and res variables from the enclosing scope of longestPalindrome
            for i in range(len(s)):
                while l>=0 and r<len(s) and s[l]==s[r]:
                    if r-l+1>max_len:
                        max_len=r-l+1
                        res=s[l:r+1]
                    l-=1
                    r+=1

        for i in range(len(s)): #using for loop not writing the same code 2 times
            sub(s,i,i) #for odd
            sub(s,i,i+1) #for even

        return res
soln=Solution()
print(soln.longestPalindrome1(s))
print(soln.longestPalindrome1(s1))
