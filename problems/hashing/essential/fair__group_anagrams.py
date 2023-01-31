from typing import List

class GroupAnagrams:
    """
    LeetCode Question Nr.49
    https://leetcode.com/problems/group-anagrams/

    Given an array of strings strs, group the anagrams together. You can return the answer in any order.
    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

    Example 1:
    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

    Example 2:
    Input: strs = [""]
    Output: [[""]]

    Example 3:
    Input: strs = ["a"]
    Output: [["a"]]
    """

    @staticmethod
    def great_ans1(strs: List[str]) -> List[List[str]]:
        """
        technique: Hash Map
        Time: O(m*n) 
        Memory: O(n)
        """
        hash = {}
        for i in strs:
            count = [0] * 26  # [0, 0, 0 ....] represent the count of [a, b, c, ...]
      
            for char in i:
                count[ord(char) - ord("a")] += 1   # ord(a)-ord(a) = 0 ; ord(b)-ord(a) = 1 ...

            tuple_count = tuple(count)
            if hash.get(tuple_count):
                hash[tuple_count].append(i) 
            else:
                hash[tuple_count] = [i]

        return hash.values()
    

    @staticmethod
    def my_solution(strs: List[str]) -> List[List[str]]:
        """
        technique: Hash Map & sort
        Time: O(m*nlogn) 
        Memory: O(n)
        """
        hash = {}
        for i in strs:
            sort_str = "".join(sorted(i))
            
            if hash.get(sort_str):
                hash[sort_str].append(i) 
            else:
                hash[sort_str] = [i]

        return hash.values()

