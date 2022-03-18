# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return None

        ans = deque()

        def helper(node, tmp):
            if node:
                if not node.left and not node.right:
                    ans.append(tmp + [node.val])
                    # print(ans)
                    return
                helper(node.left, tmp + [node.val])
                helper(node.right, tmp + [node.val])

        helper(root, [])
        size = len(ans)
        for _ in range(size):
            tmps = ans.popleft()
            ans.append('->'.join(str(j) for j in tmps))

        return ans
