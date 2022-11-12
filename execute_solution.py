from problems.Array_and_Hashing.essential import ez__two_sum
from solutions import *

from timeit import default_timer as timer
from utils.util_linked_list import transfer_list_to_linked_nodes
from utils.util_tree import transfer_list_to_binary_treenode


def execute_solution(questions, q_name):
    arg = questions[q_name][1:]

    start = timer()
    solution = questions[q_name][0](*arg)
    end = timer()
    print("===================")
    print(f"solution: {solution} \nExecuting Time: {(end-start)/0.001} ms")
    print("===================")


def solution_input():

    # questions = {question_name: [function, *function_arg]}
    questions = {'two_sum': [ez__two_sum.TwoSum.great_ans1, [2, 7, 11, 15], 18],

                 'palindrome_number_0': [PalindromeNumber.my_solution, 121],
                 'palindrome_number_1': [PalindromeNumber.great_ans1, 122],
                 'palindrome_number_2': [PalindromeNumber.great_ans2, 121],
                 'palindrome_number_3': [PalindromeNumber.great_ans3, 121],

                 'roman_to_integer_0': [RomanToInteger.my_solution, 'MCMXCIV'],
                 'roman_to_integer_1': [RomanToInteger.great_ans1, 'MCMXCIV'],

                 'longest_common_prefix_0': [LongestCommonPrefix.my_solution, ["flower","flow","flight"]],
                 'longest_common_prefix_1': [LongestCommonPrefix.great_ans1, ["flower","flow","flight"]],
                 'longest_common_prefix_2': [LongestCommonPrefix.great_ans2, ["flower","flow","flight"]],

                 'valid_parentheses_0': [ValidParentheses.my_solution, "((([]){}))"],
                 'valid_parentheses_1': [ValidParentheses.great_ans1, "()"],

                 'merge_two_sorted_lists_0': [MergeTwoSortedLists.my_solution, transfer_list_to_linked_nodes([1,2,4]), transfer_list_to_linked_nodes([1,3,4])],

                 'contains_duplicate_0': [ContainsDuplicate.my_solution, [1,2,3,1]],
                 'contains_duplicate_1': [ContainsDuplicate.great_ans1, [0,0,1,2,3]],

                 'vali_palindrome_0': [ValidPalindrome.my_solution, "A man, a plan, a canal: Panama"],
                 'vali_palindrome_1': [ValidPalindrome.great_ans1, "A man, a plan, a canal: Panama"],
                 'vali_palindrome_2': [ValidPalindrome.great_ans2, "A man, a plan, a canal: Panama"],

                 'valid_anagram_0': [ValidAnagram.my_solution, "rat", "car"],
                 'valid_anagram_1': [ValidAnagram.great_ans1, "anagram", "nagaram"],
                 'valid_anagram_2': [ValidAnagram.great_ans2, "anagram", "nagaram"],

                 'binary_search_0': [BinarySearch.my_solution, [-1,0,3,5,9,12], 2],
                 'binary_search_1': [BinarySearch.great_ans1, [-1,0,3,5,9,12], 2],

                 'best_time_to_buy_and_sell_stock_0': [BestTimeToBuyAndSellStock.my_solution, [7,1,5,3,6,4]],
                 'best_time_to_buy_and_sell_stock_1': [BestTimeToBuyAndSellStock.great_ans1, [7,1,5,3,6,4]],

                 'single_number_0': [SingleNumber.my_solution, [2,2,1]],
                 'single_number_1': [SingleNumber.great_ans1, [2,2,1]],

                 'same_tree_0': [SameTree.my_solution, transfer_list_to_binary_treenode([1,2,3]), transfer_list_to_binary_treenode([1,2,3])],
                }
    return questions


def main(q_name):
    questions = solution_input()
    execute_solution(questions, q_name)


if __name__ == '__main__':
    # input question name you want to execute as argument
    main('two_sum')

