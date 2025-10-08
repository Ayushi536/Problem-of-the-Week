from itertools import permutations
import math

def can_make_24(nums):
    EPSILON = 1e-6 

    def helper(numbers):
        if len(numbers) == 1:
            return math.isclose(numbers[0], 24, abs_tol=EPSILON)

        for i in range(len(numbers)):
            for j in range(len(numbers)):
                if i != j:
                    next_nums = [numbers[k] for k in range(len(numbers)) if k != i and k != j]
        
                    for op in ['+', '-', '*', '/']:
                        if op == '+':
                            next_nums.append(numbers[i] + numbers[j])
                        elif op == '-':
                            next_nums.append(numbers[i] - numbers[j])
                        elif op == '*':
                            next_nums.append(numbers[i] * numbers[j])
                        elif op == '/':
                            if numbers[j] == 0:  
                                continue
                            next_nums.append(numbers[i] / numbers[j])
                        
                        if helper(next_nums):
                            return True
                        next_nums.pop()  
        return False

    for perm in permutations(nums):
        if helper(list(perm)):
            return True
    return False

if __name__ == "__main__":
    nums = list(map(int, input().split())) 
    print(can_make_24(nums))
