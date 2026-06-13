class Solution:
    def customSort(self, arr):
      l=len(arr)/2
      half1=arr[:int(l)]
      half2=arr[int(l):]
      half1.sort() 
      half2.sort(reverse=True)
      result=half1+half2
      return result
                
# Example usage:
solution = Solution()      
arr = list(map(int, input().strip().split()))
print(solution.customSort(arr))