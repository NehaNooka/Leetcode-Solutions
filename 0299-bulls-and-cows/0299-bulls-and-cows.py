class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret_set=Counter(secret)
        A,B=0,0
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                A+=1
                secret_set[secret[i]]-=1
        for i in range(len(secret)):
            if secret[i]!=guess[i] and secret_set[guess[i]]>0:
                B+=1
                secret_set[guess[i]]-=1
        
        return str(A)+'A'+str(B)+'B'

        