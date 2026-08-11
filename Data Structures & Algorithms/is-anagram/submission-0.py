class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        l1 = []
        l2 = []
        for i in range (0, len(s)):
            l1.append(s[i])
            l2.append(t[i])
        l1.sort()
        l2.sort()
        if (l1 == l2):
            return True
        else : 
            return False