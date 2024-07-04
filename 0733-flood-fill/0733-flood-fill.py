class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        if not image or image[sr][sc] == color:
            return image
        starting = image[sr][sc]
        m, n = len(image), len(image[0])

        def bfs(row, col):
            if 0 <= row < m and 0 <= col < n and image[row][col] == starting:
                image[row][col] = color
                bfs(row + 1, col)
                bfs(row - 1, col)
                bfs(row, col + 1)
                bfs(row, col - 1)

        bfs(sr, sc)
        return image
