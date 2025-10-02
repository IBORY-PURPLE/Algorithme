# def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#     if not head or not head.next:
#         return head

#     n = 0
#     node = head
#     while node:
#         n += 1
#         node = node.next

#     dummy = ListNode(0, head)
#     size = 1

#     while size < n:
#         prev = dummy
#         curr = dummy.next

#         while curr:
#             head1 = curr
#             head2 = self._split(head1, size)
#             next_start = self._split(head2, size)
#             merged_head, merged_tail = self._merge(head1, head2)

#             prev.next = merged_head
#             prev = merged_tail
#             curr = next_start

#         size <<= 1

#     return dummy.next

#     def _split(self, head: Optional[ListNode], length: int) -> Optional[ListNode]:
#         if not head:
#             return None
#         for _ in range(length - 1):
#             if not head.next:
#                 break
#             head = head.next
#         rest = head.next
#         head.next = None
#         return rest

#     def _merge(self, l1: Optional[ListNode], l2: Optional[ListNode]):
#         dummy = ListNode(0)
#         tail = dummy

#         while l1 and l2:
#             if l1.val <= l2.val:
#                 tail.next, l1 = l1, l1.next
#             else:
#                 tail.next, l2 = l2, l2.next
#             tail = tail.next

#         tail.next = l1 if l1 else l2

#         while tail.next:
#             tail = tail.next

#         return dummy.next, tail

import sys

# str1 = sys.stdin.readline().strip()

# len1 = len(str1)
# for i in range(1, len1+1):
#     print(i)

from collections import deque
queue = deque([1,2,3])

print(queue)

queue.append(4)
print(queue)