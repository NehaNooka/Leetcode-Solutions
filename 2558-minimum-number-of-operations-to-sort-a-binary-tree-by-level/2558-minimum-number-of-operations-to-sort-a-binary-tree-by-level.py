from collections import deque

class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def minSwapsToSort(arr):
            # Create an array of tuples (value, original_index) and sort by value
            indexed_arr = sorted([(val, idx) for idx, val in enumerate(arr)])
            visited = [False] * len(arr)
            swaps = 0
            for i in range(len(arr)):
                # If the element is already in the correct position or visited, skip it
                if visited[i] or indexed_arr[i][1] == i:
                    continue
                # Count the size of the cycle
                cycle_size = 0
                j = i
                while not visited[j]:
                    visited[j] = True
                    j = indexed_arr[j][1]
                    cycle_size += 1
                # Add cycle size - 1 to swaps
                if cycle_size > 1:
                    swaps += cycle_size - 1
            return swaps
        minOp = 0
        q = deque([root])
        while q:
            levelEle = []
            for _ in range(len(q)):
                ele = q.popleft()
                if ele.left: q.append(ele.left)
                if ele.right: q.append(ele.right)
                levelEle.append(ele.val)
            minOp += minSwapsToSort(levelEle)
        return minOp
