def misere_nim(heaps):
    
    a, b, c = heaps
    
    # Case when all heaps are of size 1
    if a == b == c == 1:
        return False  # 3 heaps → first player loses under misère rules
    
    # General case: normal nim-sum strategy
    xor_sum = a ^ b ^ c
    return xor_sum != 0


# Examples
print(misere_nim([3, 4, 5]))  # True
print(misere_nim([1, 1, 1]))  # False
print(misere_nim([1, 1, 2]))  # True
