def fixed_point(arr):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == mid:
            return mid 
        elif arr[mid] > mid:
            right = mid - 1
        else:
            left = mid + 1
    
    return False


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    print(fixed_point(arr))
