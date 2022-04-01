class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if not image or image[sr][sc] == newColor:
            return image

        m = len(image)
        n = len(image[0])
        dir_xy = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        oldcolor = image[sr][sc]

        def dfs(i, j):
            nonlocal image
            if i >= 0 and i < m and j >= 0 and j < n and image[i][j] == oldcolor:
                image[i][j] = newColor
                for d in dir_xy:
                    n_x = d[0] + i
                    n_y = d[1] + j
                    dfs(n_x, n_y)

        dfs(sr, sc)
        return image
