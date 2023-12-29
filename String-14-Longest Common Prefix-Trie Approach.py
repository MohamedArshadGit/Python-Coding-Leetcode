'''14. Longest Common Prefix
Solved
Easy
Topics
Companies

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

Seen this question in a real interview before?
1/4
Yes
No
Accepted
2.9M
Submissions
7M
Acceptance Rate
42.0%
Topics
String
Trie'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        res=''
        count=0
        for i in range(len(strs[0])): #taking 1st word in for loop
            # edge case
            for s in strs:
                if i==len(s) or s[i]!=strs[0][i]:#i==len(s) means it reaches the end and no more word to compare or all the words are not same and s[i]!=strs[0][i] is perfix of words are not same
                    return res
            res=res+strs[0][i]
        return res

strs=["flower","flow","flight"]
soln=Solution()
print(soln.longestCommonPrefix(strs))

strs1 = ["dog","racecar","car"]
soln=Solution()
print(soln.longestCommonPrefix(strs1))

'''
chatgpt
User
what is trie dsa?
ChatGPT

A Trie, also known as a prefix tree, is a tree-like data structure used for efficient retrieval of key-value pairs where the keys are usually strings. It's particularly useful for operations involving strings or sequences, providing efficient prefix-based searches and insertions.
Structure of a Trie:

    Nodes: Each node in a Trie represents a single character. Nodes are connected by edges, and each edge represents a character in the sequence.

    Root Node: The topmost node of the Trie (often called the root) typically represents an empty string or null.

    Child Nodes: Nodes connected to the root node represent characters. Each node might have multiple children, corresponding to different characters.

    End of Word Marker: A flag often denotes the end of a valid word. This flag indicates that the sequence of characters represented by the path from the root to this node forms a complete word.

Operations in a Trie:

    Insertion: To insert a new word into a Trie, characters are added as nodes, and a marker is set at the end of the word to signify its completion.

    Search: Searching in a Trie involves traversing the tree based on the characters of the word being searched. If the complete word is found (i.e., the path from the root to a node has a marker indicating the end of a word), the search is successful.

    Prefix Search: A Trie is highly efficient for prefix-based searches. For example, finding all words starting with a specific prefix involves traversing the Trie until the prefix is reached and then exploring all words branching from that point.

    Deletion: Removing a word from a Trie requires marking the end-of-word flag appropriately and, if necessary, pruning branches that are no longer part of any valid word.

Advantages of Tries:

    Efficient Retrieval: Tries provide fast retrieval of words or strings based on prefixes.
    Prefix-Based Searches: Easily find all words with a given prefix.
    Space Efficiency: Although space-consuming compared to other data structures, Tries can efficiently store large dictionaries.
    Support for Autocomplete: Due to its prefix search capability, Tries are used extensively in autocomplete features.

Use Cases:

    Autocomplete and text suggestions in search engines or word processors.
    Dictionary implementations for fast word lookup.
    IP routing and network traffic optimization.
    Implementing algorithms like Huffman coding for data compression.

Tries are powerful data structures for string-related operations, providing efficient ways to store, retrieve, and process sequences of characters or words.

'''