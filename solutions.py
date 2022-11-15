from array import array
from typing import List
from utils.util_linked_list import ListNode, transfer_linked_nodes_to_list
from utils.util_tree import BinaryTreeNode


class PalindromeNumber:
    @staticmethod
    def my_solution(x: int) -> bool:
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

    @staticmethod
    def great_ans1(x: int) -> bool:
        """
        int is allowed to converted to str
        https://leetcode.com/problems/palindrome-number/discuss/785314/Python-3-greater-1-solution-is-89.20-faster.-2nd-is-99.14-faster.-Explanation-added
        """
        if x < 0:
            return False
        return str(x) == str(x)[::-1]

    @staticmethod
    def great_ans2(x: int) -> bool:
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

    @staticmethod
    def great_ans3(x: int) -> bool:
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


class RomanToInteger:
    @staticmethod
    def my_solution(s: str) -> int:
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

    @staticmethod
    def great_ans1(s: str) -> int:
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


class LongestCommonPrefix:
    @staticmethod
    def my_solution(strs: List[str]) -> str:
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

    @staticmethod
    def great_ans1(strs: List[str]) -> str:
        """
        With zip
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


class ValidParentheses:
    @staticmethod
    def my_solution(s: str) -> bool:
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
    
    @staticmethod
    def great_ans1(s: str) -> bool:
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


class MergeTwoSortedLists:
    @staticmethod
    def my_solution(l1: ListNode, l2: ListNode) -> ListNode:
        """
        You are given the heads of two sorted linked lists list1 and list2.
        Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
        Return the head of the merged linked list.

        Input: list1 = [1,2,4], list2 = [1,3,4]
        Output: [1,1,2,3,4,4]
        """
        dummy = ListNode()
        temp = dummy

        while l1 and l2:
            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next

            temp = temp.next
            
        if l1:
            temp.next = l1
        elif l2:
            temp.next = l2

        return transfer_linked_nodes_to_list(dummy.next) # if run on leetcode server, then simply return dummy.next

        

class BinarySearch:
    """
    Given an array of integers nums which is sorted in ascending order, 
    and an integer target, write a function to search target in nums. 
    If target exists, then return its index. Otherwise, return -1.
    You must write an algorithm with O(log n) runtime complexity.

    Input: nums = [-1,0,3,5,9,12], target = 9
    Output: 4
    Explanation: 9 exists in nums and its index is 4
    """

    @staticmethod
    def my_solution(nums: List[int], target: int) -> int:
        """
        tech use : binary search
        """
        target_index = 0
        
        while len(nums) > 1:
            split_index = int(len(nums)/2)
            
            if target < nums[split_index]:
                nums = nums[:split_index]
                target_index += 0 
            elif target > nums[split_index]:
                nums = nums[split_index:]
                target_index += split_index
            else:
                target_index += split_index
                return target_index
        
        return target_index if nums[0] == target else -1
            

    @staticmethod
    def great_ans1(nums: List[int], target: int) -> int:
        """
        tech use : binary search
        https://www.youtube.com/watch?v=s4DPM8ct1pI
        """
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2  # to prevent overfloat: mid = l + (r-l)//2
            if target < nums[mid]:
                r = mid - 1
            elif target > nums[mid]:
                l = mid + 1
            else:
                return mid
        return -1    


class SingleNumber:
    """
    Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
    You must implement a solution with a linear runtime complexity and use only constant extra space.

    Input: nums = [4,1,2,1,2]
    Output: 4
    """

    @staticmethod
    def my_solution(nums: List[int]) -> int:
        i = 0
        while i < len(nums)-1:
            if nums[i] not in nums[:i] and nums[i] not in nums[i+1:]:
                return nums[i]
            i += 1
        return nums[i]
            

    @staticmethod
    def great_ans1(nums: List[int]) -> int:
        """
        tech use : bit manipulation / XOR
        https://leetcode.com/problems/single-number/discuss/1771771/Think-it-through-oror-Time%3A-O(n)-Space%3A-O(1)-oror-Python-Explained

        XOR:
        0^0 = 0 ; 1^1 = 0 ; 1^0 = 1
        2^2 = 0 ; 2^3 = 5 
        A^B^A = A^A^B : 1^2^3^2^3 = 1 ^ (2^2) ^ (3^3) = 1^0^0 = 1
        https://accu.org/journals/overload/20/109/lewin_1915/
        """
        
        res = 0
        for num in nums:
            res = res ^ num
        
        return res


class SameTree:
    """
    https://leetcode.com/problems/same-tree/
    Given the roots of two binary trees p and q, write a function to check if they are the same or not.
    Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

    Input: p = [1,2,3], q = [1,2,3]
    Output: true
    """

    @staticmethod
    def my_solution(p: BinaryTreeNode, q: BinaryTreeNode) -> bool:
        """
        tech use : Depth First Search (DFS)
        https://www.techiedelight.com/depth-first-search/

        https://www.youtube.com/watch?time_continue=453&v=vRbbcKXCxOw&feature=emb_title
        """

        def _is_same_tree(p, q):
            if not p and not q: 
                # if both p and q are None (empty tree)
                return True
            
            if not p or not q or p.val != q.val:
                # if only one of p or q is empty or the value for both are different
                return False
        
            return (_is_same_tree(p.left, q.left) and 
                    _is_same_tree(p.right, q.right))
        
        return (_is_same_tree(p, q))
        
