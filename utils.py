
class ListNode(object):
    def __init__(self, val=0, next=None):
        if isinstance(val,int):
            self.val = val
            self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, value):
        newNode = ListNode(value)

        if self.head is None:
            self.head = newNode
        else:
            current_node = self.head

            while (current_node.next):
                # find the last existed node
                current_node = current_node.next
            
            current_node.next = newNode

    def print_list(self):
        current_node = self.head
        while (current_node):
            print(current_node.val)
            current_node = current_node.next


def transfer_list_to_linked_nodes(lst):
    head = None
    for val in reversed(lst):
        head = ListNode(val, head)
    return head


def transfer_linked_nodes_to_list(head):
    lst = []
    while head:
        lst.append(head.val)
        head = head.next
    return lst




