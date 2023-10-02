class Solution:
    def winnerOfGame(self, col: str) -> bool:
        al=0
        bo=0
        for i in range(1,len(col)-1):
            if col[i]=='A' and col[i-1]=='A' and col[i+1]=='A':
                al+=1
            elif col[i]=='B' and col[i-1]=='B' and col[i+1]=='B':
                bo+=1
        if al==0:
            return False
        elif al>bo:
            return True
        else:
            return False
                        

        