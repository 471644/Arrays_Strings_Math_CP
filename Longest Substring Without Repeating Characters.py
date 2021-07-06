'''Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''
####### Brute Force ######
from itertools import combinations
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s)<=1:
            return len(s)
        
        return max([len(s[x:y]) for x,y in combinations(range(len(s)+1),r=2) if len(set(s[x:y])) == len(s[x:y])]) 

####### O(n) Time || O(n) Space ######
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s)<=1:
            return len(s)
        else:
            start=0
            seen={}
            len_ = 0
            end=0
            while end<len(s):
                if s[end] in seen:
                    start =max(seen[s[end]],start)
                seen[s[end]] = end+1
                len_ = max(len_,(end-start)+1)
                end+=1
            return len_    