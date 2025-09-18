from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head


        # 링크드 리스트 길이를 먼저 파악
        n = 0
        node = head
        while node:
            n += 1
            node = node.next


        dummy = ListNode(0, head)
        size = 1

        while size < n:
            prev = dummy
            curr = dummy.next

            while curr:
                # 노드 분해
                head1 = curr
                head2 = self._split(head1, size)
                next_start = self._split(head2, size)

                # 노드 병합
                merged_head, merged_tail = self._merge(head1, head2)

                # 노드 연결
                prev.next = merged_head
                prev = merged_tail
                # 새로시작
                curr = next_start

            size <<= 1  # 블록 크기 두 배(비트 연산)

        return dummy.next

    def _split(self, head: Optional[ListNode], length: int) -> Optional[ListNode]:
        """
        head에서 length개 노드를 남기고 연결을 끊어줌.
        반환값은 '끊긴 뒤 남은 리스트의 시작 노드'.
        """
        if not head:
            return None
        for _ in range(length - 1):
            if not head.next:
                break
            head = head.next
        rest = head.next
        head.next = None
        return rest

    def _merge(self, l1: Optional[ListNode], l2: Optional[ListNode]):
        dummy = ListNode(0)
        tail = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                # 오른쪽 연산을 먼저해서 li의 튜플을 형성한다
                # li이 만약 2->4->none이라면 (2->4->None, 4->None)을 가리키지만 실제 저장되는 튜플은 (2참조값, 4참조값)
                tail.next, l1 = l1, l1.next
            else:
                tail.next, l2 = l2, l2.next
            tail = tail.next

        tail.next = l1 if l1 else l2

        # tail을 실제 꼬리로 이동
        while tail.next:
            tail = tail.next

        return dummy.next, tail

if __name__ == "__main__":
    n1 = ListNode(4)
    n2 = ListNode(2)
    n3 = ListNode(1)
    n4 = ListNode(3)
    n1.next = n2
    n2.next = n3
    n3.next = n4

    # 원본 linkedlist 출력
    curr = n1
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print()


    # 정렬한 linkedlist 출력
    sol = Solution()
    sorted_head = sol.sortList(n1)

    curr = sorted_head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
