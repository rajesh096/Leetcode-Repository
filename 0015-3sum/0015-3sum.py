class Solution:
    def threeSum(self, arr: List[int]) -> List[List[int]]:
        arr.sort()  
        n = len(arr)
        result = []

        
        for i in range(n - 2):
            
            if i > 0 and arr[i] == arr[i - 1]:
                continue

            
            left, right = i + 1, n - 1
            while left < right:
                current_sum = arr[i] + arr[left] + arr[right]

                if current_sum == 0:
                    result.append([arr[i], arr[left], arr[right]])

                
                    while left < right and arr[left] == arr[left + 1]:
                        left += 1
                    while left < right and arr[right] == arr[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif current_sum < 0:
                    left += 1  
                else:
                    right -= 1  

        return result