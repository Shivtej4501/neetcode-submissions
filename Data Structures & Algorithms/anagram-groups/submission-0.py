class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            w = "".join(sorted(i))
            if w in d:
                d[w].append(i)
            else:
                d[w] = [i]
        return list(d.values())
