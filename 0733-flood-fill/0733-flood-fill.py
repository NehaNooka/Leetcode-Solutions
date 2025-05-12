from collections import deque
from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        orig = image[sr][sc]
        q = deque([(sr, sc)])
        r, c = len(image), len(image[0])
        visit = {(sr, sc)} 

        while q:
            i, j = q.popleft()
            image[i][j] = color
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                newi, newj = i + dr, j + dc
                if 0 <= newi < r and 0 <= newj < c and image[newi][newj] == orig and (newi, newj) not in visit:
                    q.append((newi, newj))
                    visit.add((newi, newj)) 

        return image
