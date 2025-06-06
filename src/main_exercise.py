import unittest

def counting_sort(arr, max_value):
    count = [0] * (max_value + 1)
    output = [0] * len(arr)
    
    for num in arr:
        count[num] += 1
    
    index = 0
    for i in range(len(count)):
        while count[i] > 0:
            output[index] = i
            index += 1
            count[i] -= 1
    
    return output

def max_hamsters(S, C, hamsters):
    left, right = 0, C  
    result = 0  
    
    while left <= right:
        mid = (left + right) // 2  
        
        food_needed = []
        max_food = 0  # Максимальне значення для Counting Sort
        for i in range(C):
            food = hamsters[i][0] + hamsters[i][1] * (mid - 1)
            food_needed.append(food)
            max_food = max(max_food, food)
        
        food_needed = counting_sort(food_needed, max_food)  # Використання Counting Sort
        
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
