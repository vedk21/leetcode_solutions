#Problem: Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Sample: haystack = 'hello', needle = 'llo', Output: '100'

class Solution:
  def strStr(self, haystack: str, needle: str) -> int:
    
    if len(needle) > 0:
      if len(haystack) >= len(needle):
        for i in range(0, len(haystack)):
          if haystack[i] == needle[0]:
            found = True
            for j in range(1, len(needle)):
              if len(haystack) > i+j and haystack[i+j] == needle[j]:
                found = True
              else:
                found = False
                break
            
            if found:
              return i
        
        return -1
      else:
        return -1
    else:
      return 0

solution = Solution()
print(solution.strStr('hello', 'ell'))
