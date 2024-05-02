import re
class Solution:
    def reverseVowels(self, s: str) -> str:
        x=re.findall("[aeiouAEIOU]", s)
        x.reverse()
        l=list(s)
        j=0
        for i in range(len(l)):
            if(j<len(x)):
                if(l[i] in "aeiouAEIOU"):
                        l[i]=x[j]
                        j=j+1
            else:
                break
        rs="".join([char for char in l])
        return rs
        


