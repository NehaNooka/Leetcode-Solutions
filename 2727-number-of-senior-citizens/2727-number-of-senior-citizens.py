class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ans = sum(1 for detail in details if int(detail[11:13]) > 60)
        return ans
        