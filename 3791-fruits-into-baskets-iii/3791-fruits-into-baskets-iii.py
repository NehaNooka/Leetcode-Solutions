class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = 1 << len(baskets).bit_length()
        tree = [0] * n + baskets + [0] * (n - len(baskets))
        for i in range(n - 1, 0, -1):
            tree[i] = max(tree[i * 2], tree[i * 2 + 1])
            
        res = 0
        for fruit in fruits:
            if tree[1] < fruit:
                res += 1
                continue
            i = 0
            while i < n:
                i = i * 2 + (tree[i * 2] < fruit)
            tree[i] = 0
            while i > 1:
                i //= 2
                tree[i] = max(tree[i * 2], tree[i * 2 + 1])

        return res