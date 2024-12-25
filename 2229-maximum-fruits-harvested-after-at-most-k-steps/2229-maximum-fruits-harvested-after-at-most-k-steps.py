class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
            n = len(fruits)
            maxlen = max(fruits[-1][0], startPos)

            arr = [0] * (maxlen + 1)
            for position, amount in fruits:
                arr[position] = amount
            
            ps = [0] * (maxlen + 1)
            ps[0] = arr[0]
            for i in range(1, maxlen + 1):
                ps[i] = ps[i - 1] + arr[i]
            max_fruits = 0
            for l in range(k + 1):            
                leftStart = max(0, startPos - l)
                leftEnd = min(maxlen, startPos - l + (k - l))

                if leftStart <= leftEnd:
                    sumLeft = ps[leftEnd] - (ps[leftStart - 1] if leftStart > 0 else 0)
                else:
                    sumLeft = 0
                rightStart = max(0, startPos + l - (k - l))
                rightEnd = min(maxlen, startPos + l)
                
                if rightStart <= rightEnd:
                    sumRight = ps[rightEnd] - (ps[rightStart - 1] if rightStart > 0 else 0)
                else:
                    sumRight = 0
                max_fruits = max(max_fruits, max(sumLeft, sumRight))

            return max_fruits


