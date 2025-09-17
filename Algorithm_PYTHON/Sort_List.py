from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

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
                # 왼쪽 리스트(head1) 시작
                head1 = curr
                # head1에서 size만큼 이동하여 잘라내기
                # split 함수: 시작 노드에서 len만큼 잘라 반환, 나머지의 시작 노드를 리턴
                head2 = self._split(head1, size)
                # head2에서 size만큼 잘라 다음 덩어리의 시작을 next_start로 받음
                next_start = self._split(head2, size)

                # 두 정렬 리스트(head1, head2) 병합
                merged_head, merged_tail = self._merge(head1, head2)

                # 이전 구간과 연결
                prev.next = merged_head
                prev = merged_tail
                curr = next_start

            size <<= 1  # 블록 크기 두 배

        return dummy.next

    def _split(self, head: 'Optional[ListNode]', length: int) -> 'Optional[ListNode]':
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
        # 이제 head가 첫 블록의 마지막 노드
        rest = head.next
        head.next = None
        return rest

    def _merge(self, l1: 'Optional[ListNode]', l2: 'Optional[ListNode]'):
        """
        두 오름차순 리스트 l1, l2를 병합하여 (머리, 꼬리) 튜플로 반환.
        """
        dummy = ListNode(0)
        tail = dummy

        while l1 and l2:
            if l1.val <= l2.val:
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

    curr = n1
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print()


    sol = Solution()
    sorted_head = sol.sortList(n1)

    curr = sorted_head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
