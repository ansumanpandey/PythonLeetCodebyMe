class Solution:
    def reverseWords(self, s: str) -> str:
        txt=s.split()
        l=[x.strip(' ') for x in txt]
        l.reverse()
        rs=" ".join([x for x in l]).strip()
        return rs




