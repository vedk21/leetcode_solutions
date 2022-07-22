# Problem: Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

# Sample: s = 'hello world', Output: 'olleh dlrow'


class Solution:
  def reverseWords(self, s: str) -> str:
    
    result = ''

    words = s.strip().split(' ')

    for word in words:
      if result:
        result += ' '
      for w in range(len(word) - 1, -1, -1):
        result += word[w]
    
    return result

solution = Solution()
print(solution.reverseWords('hello world'))
