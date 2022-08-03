from typing import List


class Solution:
    def twoSum_my(self, nums: List[int], target: int) -> List[int]:
        """
        LeetCode Question Nr.1
        Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
        You may assume that each input would have exactly one solution, and you may not use the same element twice.
        You can return the answer in any order.

        Input: nums = [2,7,11,15], target = 9  Output: [0,1]
        """
        results = []
        for i in range(0, len(nums)):
            for j in range(1, len(nums)-i):
                if nums[i] + nums[i+j] == target:
                    results.extend([i, i+j])
        return results


    def twoSum_ans1(self, nums: List[int], target: int) -> List[int]:
        """
        https://leetcode.com/problems/two-sum/discuss/737092/Sum-MegaPost-Python3-Solution-with-a-detailed-explanation
        """
        results = {}
        for i, val in enumerate(nums):
            res = target - val

            if res in results:
                return [results[res], i]
            else:
                results[val] = i


    def twoSum_ans2(self, nums: List[int], target: int) -> List[int]:
        """
        In case nums has been already ascendingly sorted
        """
        right_index = len(nums) - 1
        for left_index in range(0, len(nums)-1):
            while left_index < right_index:
                sum_result = nums[left_index] + nums[right_index]
                if sum_result == target:
                    return [left_index, right_index]
                elif sum_result < target:
                    left_index += 1
                else:
                    right_index -= 1


    def palindrome_number_my(self, x: int) -> bool:
        """
        LeetCode Question Nr.9
        Given an integer x, return true if x is palindrome integer.
        An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

        Input: x = 121  Output: true
        """
        x = str(x)
        right_index = len(x) - 1
        left_index = 0
        while left_index < right_index:
            if x[left_index] == x[right_index]:
                left_index += 1
                right_index -= 1
            else:
                return False
        return True


    def palindrome_number_ans1(self, x: int) -> bool:
        """
        int is allowed to converted to str
        https://leetcode.com/problems/palindrome-number/discuss/785314/Python-3-greater-1-solution-is-89.20-faster.-2nd-is-99.14-faster.-Explanation-added
        """
        if x < 0:
            return False
        return str(x) == str(x)[::-1]


    def palindrome_number_ans2(self, x: int) -> bool:
        """
        int is not allowed to converted to str
        """
        if x < 0:
            return False

        input_nb = x
        recreate_nb = 0
        while x > 0:
            recreate_nb = recreate_nb * 10 + x%10
            x = x//10
        return recreate_nb == input_nb


    def palindrome_number_ans3(self, x: int) -> bool:
        """
        int is not allowed to converted to str & Advanced and faster solution
        """
        if x < 0 or (x > 0 and x%10 == 0):
            return False

        recreate_nb = 0
        while x > recreate_nb:
            recreate_nb = recreate_nb * 10 + x%10
            x = x//10
        return True if recreate_nb == x or recreate_nb//10 == x else False


    def roman_to_integer_my(self, s: str) -> int:
        """
        LeetCode Question Nr.13
        Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
        Symbol       Value
        I             1
        V             5
        X             10
        L             50
        C             100
        D             500
        M             1000
        Roman numerals are usually written largest to smallest from left to right.
        There are six instances where subtraction is used:
            I can be placed before V (5) and X (10) to make 4 and 9.
            X can be placed before L (50) and C (100) to make 40 and 90.
            C can be placed before D (500) and M (1000) to make 400 and 900.
        Given a roman numeral, convert it to an integer.

        Input: s = "III"  Output: 3
        Input: s = "MCMXCIV" Output: 1994
        """
        dict_normal = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        dict_subtract = {'IV': 1, 'IX': 1, 'XL': 10, 'XC': 10, 'CD': 100, 'CM': 100}

        sum_all = sum([dict_normal[s_letter] for s_letter in list(s)])
        sum_deduct = sum([dict_subtract[subtract_key] for subtract_key in dict_subtract.keys() if subtract_key in s])
        return sum_all - sum_deduct * 2


    def roman_to_integer_ans1(self, s: str) -> int:
        """
        https://leetcode.com/problems/roman-to-integer/discuss/6537/My-Straightforward-Python-Solution
        """
        dict_normal = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        result = 0
        for str_index in range(0, len(s)-1):
            former_letter_nb = dict_normal[s[str_index]]
            latter_letter_nb = dict_normal[s[str_index + 1]]
            if former_letter_nb >= latter_letter_nb:
                result += former_letter_nb
            else:
                result -= former_letter_nb
        return result + dict_normal[s[-1]]


    def longest_common_prefix_my(self, strs: List[str]) -> str:
        """
        LeetCode Question Nr.14
        Write a function to find the longest common prefix string amongst an array of strings.
        If there is no common prefix, return an empty string "".

        Input: strs=["flower","flow","flight"]  Output: "fl"
        """
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


    def longest_common_prefix_ans1(self, strs: List[str]) -> str:
        """
        With zip
        https://leetcode.com/problems/longest-common-prefix/discuss/6911/Simple-Python-solution
        """

        result = ''
        for letter_set in zip(*strs):
            if len(letter_set) == 1:
                result += letter_set[0]
            else:
                break

        return result


    def longest_common_prefix_ans2(self, strs: List[str]) -> str:
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


    def valid_parentheses_my(self, s: str) -> bool:
        """
        LeetCode Question Nr.20
        Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
        An input string is valid if:
            Open brackets must be closed by the same type of brackets.
            Open brackets must be closed in the correct order.

        Input: s = "{[]}"  Output: true
        Input: s = "([)]"  Output: false
        Input: s = "()[]{}"  Output: true
        """

        ## technic used: stack

        if len(s) <= 1:
            return False

        stack = []
        end_bracket_dict = {"]":"[", "}":"{", ")":"("}

        for char in s:
            if char in end_bracket_dict.values():
                stack.append(char)
            elif char in end_bracket_dict.keys():
                if len(stack) == 0 or end_bracket_dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []   # to avoid something like "(("
    

    def valid_parentheses_ans1(self, s: str) -> bool:
        """
        https://leetcode.com/problems/valid-parentheses/discuss/316753/Python-4ms-Faster-then-100-with-explanation
        """

        ## technic used: stack
        
        if len(s) <= 1:
            return False

        stack = []
        start_bracket_dict = {"[":"]", "{":"}", "(":")"}

        for char in s:
            if char in start_bracket_dict.keys():
                stack.append(char)
            elif char in start_bracket_dict.values():
                if len(stack) == 0 or char != start_bracket_dict[stack.pop()]:
                    return False
            else:
                return False
        
        return stack == []









