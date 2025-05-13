"""
LeetCode Problem 21: Merge Two Sorted Lists
Difficulty: Easy

Merge two sorted linked lists and return it as a new sorted list.
The new list should be made by splicing together the nodes of the first two lists.

Approach:
- Use a dummy (prehead) node to start.
- Compare current nodes of both lists and attach the smaller one to the result.
- Advance pointers as needed.
- Attach the remaining part once one list is exhausted.
"""

from typing import Optional

# ✅ Clase base utilizada por LeetCode para representar nodos de lista enlazada
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ✅ Esta es la solución esperada por LeetCode (solo esta función es evaluada)
class Solution:
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        prehead = ListNode(-1)
        current = prehead

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        current.next = list1 if list1 else list2
        return prehead.next
    
    # 🔧 Métodos de apoyo para pruebas locales (no necesarios en LeetCode)

    def build_linked_list(self,values):
        """Crea una lista enlazada a partir de una lista de valores."""
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head
    

    def print_linked_list(self,head):
        """Imprime una lista enlazada en formato legible."""
        while head:
            print(head.val, end=" → ")
            head = head.next
        print("None")


# 🧪 Prueba local
if __name__ == "__main__":
    solution = Solution()
    list1 = solution.build_linked_list([1, 2, 4])
    list2 = solution.build_linked_list([1, 3, 4])
    merged_list = solution.mergeTwoLists(list1, list2)
    solution.print_linked_list(merged_list)
