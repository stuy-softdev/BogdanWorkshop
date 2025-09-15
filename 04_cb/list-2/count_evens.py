def count_evens(nums):
    even_counter = 0
    for i in nums:
        if i%2 == 0:
            even_counter += 1
    return even_counter
    
print(count_evens([2, 1, 2, 3, 4])) # 3
print(count_evens([2, 2, 0])) # 3
print(count_evens([1, 3, 5])) # 0