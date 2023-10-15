'''49. Group Anagrams
Medium

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
 typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:

Input: strs = [""]
Output: [[""]]

Example 3:

Input: strs = ["a"]
Output: [["a"]]

Constraints:

    1 <= strs.length <= 104
    0 <= strs[i].length <= 100
    strs[i] consists of lowercase English letters.

'''


from collections import defaultdict #defaultdict is a subclass of the built-in dict class,
# and it allows you to create dictionaries with default values for keys that haven't been explicitly set.
# This can be particularly useful when you're working with dictionaries and want to avoid key errors.
def groupAnagrams(strs):
    res=defaultdict(list) #subclass of dictionary to avoid error-very important refer above
    for s in strs:
        count=[0]*26 #create 26 0's to create unique key for each word
        for c in s:
            print(ord(c), ord("a")) #ord is to find unicode value(integer) of a character
            count[ord(c)-ord("a")]+=1 #we are subtracting c word(string) from a to get value and add to 1 ,
            # u will get exactly words placed in 0's
            print(count)
        res[tuple(count)].append(s) #here we convert into tuple because default dict: list cannot be
        # accessed using keys and values so use tuple,if we didnt use it will throw error unhasable list-very important
        print(res)
    return res.values()

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
a=groupAnagrams(strs)
print(a)

#just for practise trying again
def GROUPANAGRAMS(strs):
    res=defaultdict(list)
    for s in strs:
        count=[0]*26
        for c in s:
            count[ord(c)-ord("a")]+=1
        res[tuple(count)].append(s)
    counter=0

    return res.values()
a=GROUPANAGRAMS(strs)
print(a)
