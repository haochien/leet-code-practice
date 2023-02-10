from problems.array.essenstial import ez__plus_one
from problems.hashing.essential import ez__two_sum, ez__contain_duplicate, ez__valid_anagram, fair__group_anagrams
from problems.two_pointers.essential import ez__valid_palindrome, ez__Remove_Duplicates_from_Sorted_Array, ez__merge_sorted_array, fair__two_sum_input_sorted
from problems.sliding_window.essential import ez__best_time_to_buy_and_sell_stock, fair__longest_substring_without_repeat
from problems.dynamic_programming_1d.essential import ez__climbing_stairs, ez__min_cost_climbing_stairs, fair__house_robber, fair__house_robber2
from problems.dynamic_programming_2d.essensial import fair__unique_paths
from problems.stack.essential import ez__valid_parentheses, fair__min_stack
from problems.binary_search.essential import ez__binary_search, ez__sqrt
from problems.bit_manipulation.essential import ez__single_value, ez__number_of_1_bits
from problems.linked_list.essential import ez__merge_two_sorted_list
from problems.trees.esenstial import ez__same_tree, ez__binary_tree_inorder_traversal, ez__symmetric_tree, ez__max_depth_of_binary_tree, \
                                     ez__sorted_array_to_binary_search_tree
from problems.string_problems.essential import ez__longest_common_prefix, ez__roman_to_integer
from problems.heap_priority_queue.essential import fair__kth_largest_element_in_a_stream
from problems.graphs.essensial import fair__number_of_islands
from problems.backtracking.essential import fair__subsets
from problems.greedy.essential import fair__max_subarray

from problems.two_pointers.rest import ez__palindronme_number

from timeit import default_timer as timer
from utils.util_linked_list import transfer_list_to_linked_nodes
from utils.util_tree import transfer_list_to_binary_treenode


def execute_solution(questions, q_name):
    arg = questions[q_name][1:]

    start = timer()
    if isinstance(questions[q_name][0], type):  # check whether the solution is written in class format
        solution = questions[q_name][0](*arg).execute()
    else:
        solution = questions[q_name][0](*arg)
    end = timer()

    print("===================")
    print(f"solution: {solution} \nExecuting Time: {(end-start)/0.001} ms")
    print("===================")


def solution_input():

    # questions = {question_name: [function, *function_arg]}
    questions = {

                 ## ===== General Array =====
                 # imp: ***
                 'plus_one': [ez__plus_one.PlusOne.my_solution, [1, 2, 3]],


                 ## ===== Array and Hashing =====
                 # imp: ***
                 'two_sum': [ez__two_sum.TwoSum.great_ans1, [2, 7, 11, 15], 18],
                 'contains_duplicate': [ez__contain_duplicate.ContainsDuplicate.great_ans1, [0,0,1,2,3]],

                 'group_anagrams': [fair__group_anagrams.GroupAnagrams.great_ans1, ["eat","tea","tan","ate","nat","bat"]],

                 # imp: **      
                 'valid_anagram': [ez__valid_anagram.ValidAnagram.great_ans1, "anagram", "nagaram"],


                 ## ===== Two Pointers =====
                 # imp: ***
                 'vali_palindrome': [ez__valid_palindrome.ValidPalindrome.great_ans1, "A man, a plan, a canal: Panama"],
                 'remove_duplicates_from_sorted_array': [ez__Remove_Duplicates_from_Sorted_Array.RemoveDuplicatesFromSortedArray.great_ans1, [0,0,1,1,1,2,2,3,3,4]],
                 'merge_sorted_array': [ez__merge_sorted_array.MergeSortedArray.great_ans1, [1,2,3,0,0,0], 3, [2,5,6], 3],
                 'two_sum_input_sorted': [fair__two_sum_input_sorted.TwoSumInputSorted.my_solution, [2,7,11,15], 9],
                 # imp: *
                 'palindrome_number': [ez__palindronme_number.PalindromeNumber.my_solution, 121], 


                 ## ===== Sliding Window =====
                 # imp: ***
                 'best_time_to_buy_and_sell_stock': [ez__best_time_to_buy_and_sell_stock.BestTimeToBuyAndSellStock.great_ans1, [7,1,5,3,6,4]],
                 'longest_substring_without_repeat': [fair__longest_substring_without_repeat.LongestSubstringWithoutRepeat.great_ans1, "dvdf"],


                 ## ===== Dynamic Programming 1D =====
                 # imp: ***
                 'climbing_stairs': [ez__climbing_stairs.ClimbingStairs.great_ans2, 4],
                 'min_cost_climbing_stairs': [ez__min_cost_climbing_stairs.MinCostClimbingStairs.great_ans1, [10,15,20]], 
                 
                 'house_robber': [fair__house_robber.HouseRobber.great_ans1, [4,7,8,6,10,20,1]], 
                 'house_robber2': [fair__house_robber2.HouseRobber2.great_ans1, [1,3,1,3,100]], 


                 ## ===== Dynamic Programming 2D =====
                 # imp: ***
                 'unique_paths': [fair__unique_paths.UniquePaths.great_ans1, 3, 7],

                                
                 ## ===== Stack =====
                 # imp: ***
                 'valid_parentheses': [ez__valid_parentheses.ValidParentheses.my_solution, "((([]){}))"],
                 'min_stack': [fair__min_stack.MinStack.MySolution],    


                 ## ===== Binary Search =====
                 # imp: ***
                 'binary_search': [ez__binary_search.BinarySearch.great_ans1, [-1,0,3,5,9,12], 2],
                 'sqrt': [ez__sqrt.Sqrt.great_ans1, 8],


                 ## ===== Bit Manipulation =====
                 # imp: ***
                 'single_number': [ez__single_value.SingleNumber.great_ans1, [2,2,1]],
                 'number_of_1_bits': [ez__number_of_1_bits.NumberOfOneBits.great_ans1, 0b00000000000000000000000000001011],


                 ## ===== Linked List =====
                 # imp: ***
                 'merge_two_sorted_lists': [ez__merge_two_sorted_list.MergeTwoSortedLists.my_solution, 
                                            transfer_list_to_linked_nodes([1,2,4]), transfer_list_to_linked_nodes([1,3,4])],


                 ## ===== Trees =====
                 # imp: ***
                 'same_tree': [ez__same_tree.SameTree.my_solution, transfer_list_to_binary_treenode([1,2,3]), 
                               transfer_list_to_binary_treenode([1,2,3])],                           
                 'binary_tree_inorder_traversal': [ez__binary_tree_inorder_traversal.BinaryTreeInorderTraversal.great_ans1, 
                               transfer_list_to_binary_treenode([1,None,2,None,None,3,None])],
                 'symmetric_tree': [ez__symmetric_tree.SymmetricTree.great_ans2, transfer_list_to_binary_treenode([1,2,2,3,4,4,3])],
                 'max_depth_binary_tree': [ez__max_depth_of_binary_tree.MaxDepthBinaryTree.great_ans2, 
                               transfer_list_to_binary_treenode([3,9,20,None,None,15,7])],
                 'sorted_array_to_bst': [ez__sorted_array_to_binary_search_tree.SortedArrayToBST.great_ans1, [-10,-3,0,5,9]],               


                 ## ===== Heap / Priority Queue =====
                 # imp: ***
                 'kth_largest_in_a_stream': [fair__kth_largest_element_in_a_stream.KthLargestInStream.GreatAns1, 3, [4, 5, 8, 2], 
                                             [3, 5, 10, 9, 4]],       


                 ## ===== Graph Problems =====
                 # imp: ***
                 'number_of_islands': [fair__number_of_islands.NumberOfIslands.great_ans1, 
                                        [["1","1","0","0","0"], ["1","1","0","0","0"], ["0","0","1","0","0"], ["0","0","0","1","1"]]],            


                 ## ===== Backtracking Problems =====
                 # imp: ***
                 'subsets': [fair__subsets.Subsets.great_ans1, [1,2,3]],   


                 ## ===== Greedy Problems =====
                 # imp: ***
                 'max_subarray': [fair__max_subarray.MaxSubarray.my_solution, [-2,1,-3,4,-1,2,1,-5,4]],   
                 

                 ## ===== String Problems =====
                 # imp: ***
                 'longest_common_prefix': [ez__longest_common_prefix.LongestCommonPrefix.great_ans1, ["flower","flow","flight"]],
                 'roman_to_integer': [ez__roman_to_integer.RomanToInteger.great_ans1, 'MCMXCIV'],

                }
    return questions


def main(q_name):
    questions = solution_input()
    execute_solution(questions, q_name)


if __name__ == '__main__':
    # input question name you want to execute as argument
    main('max_subarray')

