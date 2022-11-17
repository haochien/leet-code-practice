from utils.util_linked_list import ListNode, transfer_linked_nodes_to_list

class MergeTwoSortedLists:
    """
    LeetCode Question Nr.21
    https://leetcode.com/problems/merge-two-sorted-lists/

    You are given the heads of two sorted linked lists list1 and list2.
    Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
    Return the head of the merged linked list.

    Input: list1 = [1,2,4], list2 = [1,3,4]    Output: [1,1,2,3,4,4]
    """

    @staticmethod
    def my_solution(l1: ListNode, l2: ListNode) -> ListNode:
        """
        technique: binary search
        Time: O(n)
        Memory: O(1)

        great reference:
        https://www.youtube.com/watch?v=XIdigk956u0 
        """

        dummy = ListNode()  # this is the first dummy node to prevent edge case, and it also represents the head of the final merged list
        temp = dummy   # this is simply used to represent the shifted node 

        while l1 and l2:
            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next

            temp = temp.next  # node shifted
            
        if l1:
            temp.next = l1
        elif l2:
            temp.next = l2

        return transfer_linked_nodes_to_list(dummy.next) # if run on leetcode server, then simply return dummy.next