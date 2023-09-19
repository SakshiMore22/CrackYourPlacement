class Solution:
    def maximumTime(self, time: str) -> str:
        st=''
        for i in range(len(time)):
            if i==0 and time[i]=='?':
                if time[i+1]=='?' or int(time[i+1])<4:
                    st+='2'
                else:
                    st+='1'
            elif i==1 and time[i]=='?':
                if st[i-1]!='2':
                    st+='9'
                else:
                    st+='3'
            elif i==3 and time[i]=='?':
                st+='5'
            elif i==4 and time[i]=='?':
                st+='9'
            else:
                st+=time[i]
        return st
