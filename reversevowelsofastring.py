class Solution:
    def reverseVowels(self, s: str) -> str:

        a = list(s)
        i = 0
        j = len(s)-1
        v = {'a','e','i','o','u','A','E','I','O','U'}
        while i<j:
            if a[i] in v and a[j]  in v:
                a[i],a[j] = a[j],a[i]
                i+=1
                j-=1
            elif a[i] in v:
                j-=1
            elif a[j]  in v:
                i+=1
            else:
                i+=1
                j-=1
        return "".join(a)