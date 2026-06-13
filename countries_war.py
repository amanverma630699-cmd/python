"Given two arrays of integers, arr1 and arr2, representing the strength of two countries in a war, determine wh"
"ich country is stronger. The strength of a country is determined by comparing the corresponding elements of the t"
"wo arrays. If arr1[i] > arr2[i], then country A gets a point. If arr1[i] < arr2[i], then country B gets a point. If "
"arr1[i] == arr2[i], neither country gets a point. The country with the most points at the end wins. If both countries "
"have the same number of points, it's a draw."


class Solution:

    def countryAtWar(self, arr1, arr2):
        a=0
        b=0
        for i in range(len(arr1)):
             if arr1[i]>arr2[i]:
                 a+=1
             if arr1[i]<arr2[i]:
                 b+=1
        if a>b:
            return("A")
        elif a<b:
            return("B")
        else:
             return("DRAW")
        
# Example usage:
solution = Solution()   
arr1 = list(map(int, input().strip().split()))
arr2 = list(map(int, input().strip().split()))
print(solution.countryAtWar(arr1, arr2)) 