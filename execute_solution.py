from solutions import *
from timeit import default_timer as timer
from utils import transfer_list_to_linked_nodes


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
    questions = {'twoSum_0': [TwoSum.my_solution, [2, 7, 11, 15], 9],
                 'twoSum_1': [TwoSum.great_ans1, [2, 7, 11, 15], 18],
                 'twoSum_2': [TwoSum.great_ans2, [2, 7, 11, 15], 9],

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

                'merge_two_sorted_lists': [MergeTwoSortedLists.my_solution, transfer_list_to_linked_nodes([1,2,4]), transfer_list_to_linked_nodes([1,3,4])],
                 }
    return questions


def main(q_name):
    questions = solution_input()
    execute_solution(questions, q_name)


if __name__ == '__main__':
    # input question name you want to execute as argument
    main('merge_two_sorted_lists')

