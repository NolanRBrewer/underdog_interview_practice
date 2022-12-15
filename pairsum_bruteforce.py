def solve_for_k(numbers,k):
    for num_1 in numbers:
        for num_2 in numbers:
            if num_1 != num_2 and num_1 + num_2 == k:
                k_pair = [num_1,num_2]
                return k_pair

numbers = [1,9,6,3,5,4,]
k = 10

print(solve_for_k(numbers,k))