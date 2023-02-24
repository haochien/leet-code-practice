from utils.util_linked_list import ListNode, transfer_linked_nodes_to_list

class ReorderList:
    """
    LeetCode Question Nr.143
    https://leetcode.com/problems/reorder-list/

    You are given the head of a singly linked-list. The list can be represented as:
    L0 → L1 → … → Ln - 1 → Ln
    Reorder the list to be on the following form:
    L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
    You may not modify the values in the list's nodes. Only nodes themselves may be changed.

    Example 1:
    Input: head = [1,2,3,4]
    Output: [1,4,2,3]

    Example 2:
    Input: head = [1,2,3,4,5]
    utput: [1,5,2,4,3]
    """
    @staticmethod
    def great_ans1(head: ListNode) -> None:
        """
        Time: O(n)
        Memory: O(n)
        """

        # find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        second = slow.next
        slow.next = None

        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge two halfs
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        return



    @staticmethod
    def my_solution(head: ListNode) -> None:
        """
        Time: O(n)
        Memory: O(n)
        """

        stack = []
        node = head
        while node:
            stack.append(node)
            node = node.next

        l, r = 0, len(stack) - 1
        final_node = None
        while l < r:
            stack[l].next = stack[r]
            l += 1

            if l != r:
                stack[r].next = stack[l]
                r -= 1

            final_node = stack[l] if l != r else stack[r]

        if final_node:
            final_node.next = None