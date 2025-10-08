import bisect

def length_of_LIS(arr):
    temp = []
    for num in arr:
        idx = bisect.bisect_left(temp, num)
        if idx == len(temp):
            temp.append(num)
        else:
            temp[idx] = num
    return len(temp)

if __name__ == "__main__":
    arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    print(length_of_LIS(arr)) 