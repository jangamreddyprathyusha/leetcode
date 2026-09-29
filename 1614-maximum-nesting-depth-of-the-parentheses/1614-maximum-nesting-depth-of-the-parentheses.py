class Solution(object):
    def maxDepth(self, s):
        ans=0
        count=0
        for i in s:
            if i=='(':
                count+=1
                ans=max(ans,count)
            elif i==')':
                count-=1
        return ans

        