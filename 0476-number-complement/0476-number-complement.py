class Solution(object):
    def findComplement(self, num):
        m=1
        while m<num:
            m=(m<<1)|1
        return num^m