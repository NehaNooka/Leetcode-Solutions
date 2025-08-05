class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        for fruit in fruits:
            for j in range(len(baskets)):
                if baskets[j]>= fruit:
                    baskets.pop(j)
                    break
        return len(baskets)