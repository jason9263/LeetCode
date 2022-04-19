class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        seen = set()

        def helper(i, j, index):
            if index == len(word):
                return True

            if (i < 0 or j < 0 or i >= m or j >= n or board[i][j] != word[index] or (i, j) in seen):
                return False
            else:
                seen.add((i, j))
                ans = helper(i + 1, j, index + 1) or helper(i - 1, j, index +
                                                            1) or helper(i, j - 1, index + 1) or helper(i, j + 1, index + 1)
                seen.remove((i, j))

                return ans

        for i in range(m):
            for j in range(n):
                if helper(i, j, 0):
                    return True

        return False
