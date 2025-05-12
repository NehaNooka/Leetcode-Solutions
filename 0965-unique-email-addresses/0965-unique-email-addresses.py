class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res=set()
        def format_first(l):
            res=''
            for c in l:
                if c=='+': return res
                elif c=='.': continue
                else: res+=c
            return res

        for email in emails:
            e=email.split('@')
            localname=format_first(e[0])
            ele=localname +'@'+ e[1]
            res.add(ele)
        return len(res)
        