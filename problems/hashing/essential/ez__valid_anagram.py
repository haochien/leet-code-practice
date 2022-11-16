from typing import List

class ValidAnagram:
    """
    LeetCode Question Nr.242
    https://leetcode.com/problems/valid-anagram/

    Given two strings s and t, return true if t is an anagram of s, and false otherwise.
    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
    typically using all the original letters exactly once.

    Input: s = "anagram", t = "nagaram"  Output: true
    Input: s = "rat", t = "car"  Output: false
    """

    @staticmethod
    def great_ans1(s: str, t: str) -> bool:
        """
        technique: Hash Map
        Time: O(n) : looping cause O(n) and Hashmap contribute O(1) (average : O(1)  ; worst case (collision) O(n/k))
        Memory: O(n)
        https://www.youtube.com/watch?v=9UtInBqnCgA
        """
        # following codes can be replaced by this in python:
        # Counter(s) == Counter(t)

        if len(s) != len(t):
            return False
        
        hash_s, hash_t = {}, {}

        for i in range(len(s)):
            hash_s[s[i]] = hash_s.get(s[i], 0) + 1   # .get(s[i], 0) --> return 0 if the key doesn't exist yet
            hash_t[t[i]] = hash_t.get(t[i], 0) + 1
        
        # here can be replaced by:  return hash_s == hash_t
        for key in hash_s:
            if hash_s[key] != hash_t.get(key, 0):
                return False

        return True
    

    @staticmethod
    def great_ans2(s: str, t: str) -> bool:
        """
        technique: Sort
        Time: O(logn) : sorting (Timsort) contribute additional more
        Memory: O(1)
        https://www.youtube.com/watch?v=9UtInBqnCgA
        """
        return sorted(s) == sorted(t)
    

    @staticmethod
    def my_solution(s: str, t: str) -> bool:
        """
        tech use: sort / hash table
        """
        # using sort:
        # s_sort = [i for i in s]
        # t_sort = [i for i in t]
        # s_sort.sort() 
        # t_sort.sort()
        # return s_sort == t_sort

        # without sort:
        def _create_hash(str_input):
            str_hash = {}
            for i in str_input:
                if i not in str_hash:
                    str_hash[i] = 1
                else:
                    str_hash[i] += 1
            return str_hash

        s_hash = _create_hash(s)
        t_hash = _create_hash(t)

        return s_hash == t_hash
        