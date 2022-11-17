
class RomanToInteger:
    """
    LeetCode Question Nr.13
    https://leetcode.com/problems/roman-to-integer/

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

    @staticmethod
    def great_ans1(s: str) -> int:
        """
        The trick is that the last letter is always added. Except the last one, 
        if one letter is less than its latter one, this letter is subtracted.

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


    @staticmethod
    def great_ans2(s: str) -> int:
        """
        https://leetcode.com/problems/roman-to-integer/solutions/264743/clean-python-beats-99-78/
        """
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += translations[char]
        return number


    @staticmethod
    def my_solution(s: str) -> int:
        """
        The idea for this solution has 3 steps:

        convert each letter to number and sum up
        identify dedution letter in the string and sum them up
        step1 - step 2 * 2 (in step 1, we also add deduction letter in it, so we need to deduct it twice)
        for example:
        MCMXCIV:
        sum_all = 1000+100+1000+10+100+1+5 = 2216
        sum_deduct = 100 (for CM) + 10 (for XC) + 1 (for IV) = 111
        result = 2216 - 111 * 2 = 1994
        """

        dict_normal = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        dict_subtract = {'IV': 1, 'IX': 1, 'XL': 10, 'XC': 10, 'CD': 100, 'CM': 100}

        sum_all = sum([dict_normal[s_letter] for s_letter in list(s)])
        sum_deduct = sum([dict_subtract[subtract_key] for subtract_key in dict_subtract.keys() if subtract_key in s])
        return sum_all - sum_deduct * 2
