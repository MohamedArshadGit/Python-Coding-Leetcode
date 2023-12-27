'''28. Find the Index of the First Occurrence in a String
Solved
Easy
Topics
Companies

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.



Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.



Constraints:

    1 <= haystack.length, needle.length <= 104
    haystack and needle consist of only lowercase English characters.

Seen this question in a real interview before?
1/4
Yes
No
Accepted
2.1M
Submissions
5.2M
Acceptance Rate
41.1%
Topics
Two Pointers
String
String Matching'''




class Solution(object):
    def strStr(self, haystack, needle):
        for i in range(len(haystack)+1-len(needle)): #very imp eg for haystack1 = "leetcode"
        # needle1 = "leeto" if we just give len of haystack in for loop leetc,eetco,etcod,tcode 4 loops is
        #enough but haystack1 length is 8 so it run for 8 times and shows index out of range
        #so this is a VERY IMPORTANT TECHNIQUE +1-LEN(SOMETHING) seen in 2 or 3 problems so rem this IMP!!!

            if haystack[i:i+len(needle)]==needle: #i+len(needle) VERY IMP-bcos if we just give len(needle) it will shirnk as we go on
                #eg 1st itr-leetc,2nd itr-eetc then etc then it stops tis is wrong
                #so if we give[i:i+len(needle] it will print leetc,eetco,etcod,tcode -VERY IMPORTANT
                return i
        return -1


haystack="sadbutsad"
needle="sad"
haystack1 = "leetcode"
needle1 = "leeto"
haystack2 ="hello"
needle2 ="ll"
soln=Solution()
print(soln.strStr(haystack,needle))
print(soln.strStr(haystack1,needle1))
print(soln.strStr(haystack2,needle2))

