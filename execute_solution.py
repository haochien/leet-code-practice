from problems.hashing.essential import ez__two_sum, ez__contain_duplicate, ez__valid_anagram
from problems.two_pointers.essential import ez__valid_palindrome
from problems.sliding_window.essential import ez__best_time_to_buy_and_sell_stock
from problems.stack.essential import ez__valid_parentheses
from problems.binary_search.essential import ez__binary_search
from problems.bit_manipulation.essential import ez__single_value
from problems.linked_list.essential import ez__merge_two_sorted_list

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
    questions = {
                 ## ===== Array and Hashing =====
                 # imp: ***
                 'two_sum': [ez__two_sum.TwoSum.great_ans1, [2, 7, 11, 15], 18],
                 'contains_duplicate': [ez__contain_duplicate.ContainsDuplicate.great_ans1, [0,0,1,2,3]],
                 # imp: **      
                 'valid_anagram': [ez__valid_anagram.ValidAnagram.great_ans1, "anagram", "nagaram"],


                 ## ===== Two Pointers =====
                 # imp: ***
                 'vali_palindrome': [ez__valid_palindrome.ValidPalindrome.great_ans1, "A man, a plan, a canal: Panama"], 


                 ## ===== Sliding Window =====
                 # imp: ***
                 'best_time_to_buy_and_sell_stock': [ez__best_time_to_buy_and_sell_stock.BestTimeToBuyAndSellStock.great_ans1, [7,1,5,3,6,4]],
                 

                 ## ===== Stack =====
                 # imp: ***
                 'valid_parentheses': [ez__valid_parentheses.ValidParentheses.my_solution, "((([]){}))"],


                 ## ===== Binary Search =====
                 # imp: ***
                 'binary_search': [ez__binary_search.BinarySearch.great_ans1, [-1,0,3,5,9,12], 2],


                 ## ===== Bit Manipulation =====
                 # imp: ***
                 'single_number': [ez__single_value.SingleNumber.great_ans1, [2,2,1]],
                 

                 ## ===== Linked List =====
                 # imp: ***
                 'merge_two_sorted_lists': [ez__merge_two_sorted_list.MergeTwoSortedLists.my_solution, 
                                            transfer_list_to_linked_nodes([1,2,4]), transfer_list_to_linked_nodes([1,3,4])],

                 'palindrome_number_0': [PalindromeNumber.my_solution, 121],
                 'palindrome_number_1': [PalindromeNumber.great_ans1, 122],
                 'palindrome_number_2': [PalindromeNumber.great_ans2, 121],
                 'palindrome_number_3': [PalindromeNumber.great_ans3, 121],

                 'roman_to_integer_0': [RomanToInteger.my_solution, 'MCMXCIV'],
                 'roman_to_integer_1': [RomanToInteger.great_ans1, 'MCMXCIV'],

                 'longest_common_prefix_0': [LongestCommonPrefix.my_solution, ["flower","flow","flight"]],
                 'longest_common_prefix_1': [LongestCommonPrefix.great_ans1, ["flower","flow","flight"]],
                 'longest_common_prefix_2': [LongestCommonPrefix.great_ans2, ["flower","flow","flight"]],

                 
                 'same_tree_0': [SameTree.my_solution, transfer_list_to_binary_treenode([1,2,3]), transfer_list_to_binary_treenode([1,2,3])],
                }
    return questions


def main(q_name):
    questions = solution_input()
    execute_solution(questions, q_name)


if __name__ == '__main__':
    # input question name you want to execute as argument
    main('merge_two_sorted_lists')

