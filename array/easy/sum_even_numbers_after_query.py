# Problem: We have an array A of integers, and an array queries of queries. For the i-th query val = queries[i][0], index = queries[i][1], we add val to A[index].  Then, the answer to the i-th query is the sum of the even values of A. (Here, the given index = queries[i][1] is a 0-based index, and each query permanently modifies the array A.) Return the answer to all queries.  Your answer array should have answer[i] as the answer to the i-th query.

# Sample: A = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]], Output: [8,6,2,4]

from typing import List

class Solution:
  def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
    result = []
    totalSum = sum(ele for ele in A if ele % 2 == 0)

    for i in range(len(queries)):
      val = queries[i][0]
      index = queries[i][1]

      if A[index] % 2 == 0:
        totalSum -= A[index]

      res_i_sum = A[index] + val
      if res_i_sum % 2 == 0:
        totalSum += res_i_sum

      A[index] = res_i_sum
      
      result.append(totalSum)
    
    return result

solution = Solution()
print(solution.sumEvenAfterQueries([1,2,3,4], [[1,0],[-3,1],[-4,0],[2,3]]))
