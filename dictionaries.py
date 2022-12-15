nums = [1,2,3,1,1,3,1]
good_pairs = {}

for num in nums:
    if num not in good_pairs:
        good_pairs[num] = nums.find(num)
    elif num in good_pairs: 
        
print(good_pairs)