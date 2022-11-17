
class ValidParentheses:
    """
    LeetCode Question Nr.20
    https://leetcode.com/problems/valid-parentheses/
    
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
    An input string is valid if:
        Open brackets must be closed by the same type of brackets.
        Open brackets must be closed in the correct order.

    Input: s = "{[]}"  Output: true
    Input: s = "([)]"  Output: false
    Input: s = "()[]{}"  Output: true
    """
    @staticmethod
    def my_solution(s: str) -> bool:
        """
        tech use : stack
        Time: O(n)
        Memory: O(n)
        """

        if len(s) <= 1:
            return False

        stack = []
        end_bracket_dict = {"]":"[", "}":"{", ")":"("}

        for char in s:
            if char in end_bracket_dict.values():
                stack.append(char)
            elif char in end_bracket_dict.keys():
                if len(stack) == 0 or stack.pop() != end_bracket_dict[char]:
                    return False
            else:
                return False
        return stack == []   # if all parentheses work correctly, the stack should be empty


    @staticmethod
    def great_ans1(s: str) -> bool:
        """
        tech use : stack
        Time: O(n)
        Memory: O(n)
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



    
