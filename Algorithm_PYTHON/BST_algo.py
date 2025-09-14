from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left: 'TreeNode'=None, right: 'TreeNode'=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums: List[int]) -> Optional[TreeNode]:
    def build(l: int, r: int) -> Optional[TreeNode]:
        if l > r:
            return None
        mid = (l+r) // 2
        node = TreeNode(nums[mid])
        node.left = build(l, mid - 1)
        node.right = build(mid + 1, r)
        return node
    return build(0, len(nums) -1)

def inorder(node: Optional[TreeNode]) -> List[int]:
    if not node:
        return []
    return inorder(node.left) + [node.val] + inorder(node.right)

from collections import deque
from typing import List, Optional

def serialize_level_order(root: Optional['TreeNode']) -> List[Optional[int]]:
    if not root:
        return []
    q = deque([root])
    out: List[Optional[int]] = []
    while q:
        node = q.popleft()
        if node:
            out.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            out.append(None)
    # 뒤쪽의 불필요한 None 제거
    while out and out[-1] is None:
        out.pop()
    return out


if __name__ == "__main__":
    nums = [-10, -3, 0, 5, 9]
    root = sortedArrayToBST(nums)

    print("In-order   :", inorder(root))
    print("Level-order(serialized):", serialize_level_order(root))