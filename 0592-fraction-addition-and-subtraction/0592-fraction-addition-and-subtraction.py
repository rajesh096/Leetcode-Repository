from math import gcd
class Solution:
    def fractionAddition(self, expression: str) -> str:
        def simplify(numerator, denominator):
            g = gcd(numerator, denominator)  
            return numerator // g, denominator // g  
    
        result_num, result_den = 0, 1  
        
        i = 0
        while i < len(expression):
            sign = 1  
            
            if expression[i] in "+-": 
                if expression[i] == '-':
                    sign = -1
                i += 1  
            
            
            num_start = i
            while expression[i] != '/':
                i += 1
            numerator = int(expression[num_start:i])
            
            i += 1 
            
            
            den_start = i
            while i < len(expression) and expression[i] not in "+-":
                i += 1
            denominator = int(expression[den_start:i])
            
           
            result_num = result_num * denominator + sign * numerator * result_den
            result_den = result_den * denominator
            
            
            result_num, result_den = simplify(result_num, result_den)
        
        #
        if result_den < 0:
            result_num = -result_num
            result_den = -result_den
        
        return f"{result_num}/{result_den}" if result_den != 1 else f"{result_num}/1"

