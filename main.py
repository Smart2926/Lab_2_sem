import unittest

def max_hamsters(S, C, hamsters):
    left, right = 0, C  
    result = 0  
    
    while left <= right:
        mid = (left + right) // 2  
        
        food_needed = []
        for i in range(C):
            food_needed.append(hamsters[i][0] + hamsters[i][1] * (mid - 1))
        
        for i in range(len(food_needed) - 1):
            for j in range(len(food_needed) - i - 1):
                if food_needed[j] > food_needed[j + 1]:
                    food_needed[j], food_needed[j + 1] = food_needed[j + 1], food_needed[j]  
        
        total = 0
        for i in range(mid):
            total += food_needed[i]
            if total > S:
                break
        
        if total <= S:  
            result = mid  
            left = mid + 1 
        else:
            right = mid - 1  
    
    return result
