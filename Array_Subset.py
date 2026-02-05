class Solution:
    def isSubset(self, a, b):
        freq = {}
        for i in a:
            freq[i]=freq.get(i,0)+1
        
        for i in b:
            if freq.get(i,0)==0:
                return False
            else : freq[i]=freq.get(i,0)-1
        return True