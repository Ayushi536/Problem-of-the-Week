def min_broadcast_range(listeners, towers):
    listeners.sort()
    towers.sort()
    
    def closest_tower_distance(pos):
        left, right = 0, len(towers) - 1
        res = float('inf')
        while left <= right:
            mid = (left + right) // 2
            res = min(res, abs(towers[mid] - pos))
            if towers[mid] < pos:
                left = mid + 1
            else:
                right = mid - 1
        return res

    min_range = 0
    for l in listeners:
        min_range = max(min_range, closest_tower_distance(l))
    
    return min_range


if __name__ == "__main__":
    N = int(input())
    listeners = list(map(int, input().split()))
    M = int(input())
    towers = list(map(int, input().split()))
    print(min_broadcast_range(listeners, towers))
