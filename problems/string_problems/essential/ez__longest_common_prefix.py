from typing import List

class LongestCommonPrefix:
    """
    LeetCode Question Nr.14
    https://leetcode.com/problems/longest-common-prefix/

    Write a function to find the longest common prefix string amongst an array of strings.
    If there is no common prefix, return an empty string "".

    Input: strs=["flower","flow","flight"]  Output: "fl"
    Input: strs = ["dog","racecar","car"]  Output: ""
    """

    @staticmethod
    def great_ans1(strs: List[str]) -> str:
        """
        technique: zip
        Time: O(n)
        Memory: O(n)
        https://leetcode.com/problems/longest-common-prefix/discuss/6911/Simple-Python-solution
        """
        result = ''
        for letter_set in zip(*strs):
            if len(set(letter_set)) == 1:
                result += letter_set[0]
            else:
                break

        return result


    @staticmethod
    def great_ans2(strs: List[str]) -> str:
        """
        With enumerate and loop
        https://leetcode.com/problems/longest-common-prefix/discuss/6918/Short-Python-Solution
        """
        shortest_word = min(strs, key=len)
        for index, letter in enumerate(shortest_word):
            for word in strs:
                if letter != word[index]:
                    return shortest_word[:index]
        return shortest_word
    

    @staticmethod
    def my_solution(strs: List[str]) -> str:
        shortest_str_len = min([len(word) for word in strs])
        if shortest_str_len == 0:
            return ''

        str_index = 0
        results = ''
        while str_index <= shortest_str_len-1:
            #if all([word[str_index] == strs[0][str_index] for word in strs]):
            if len(set([word[str_index] for word in strs])) == 1:
                results += strs[0][str_index]
                str_index += 1
            else:
                break
        return results





