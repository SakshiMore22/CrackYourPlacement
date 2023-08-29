class Solution:
    def bestClosingTime(self, s: str) -> int:
        n=len(s)
        ind,maxscore,score=-1,0,0
        for i in range(n):
            if s[i]=='Y':
                score+=1
            else:
                score-=1
            if score>maxscore:
                maxscore=score
                ind=i
        return ind+1