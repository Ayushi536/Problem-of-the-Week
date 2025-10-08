def knight_probability(r, c, k):
    moves = [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]
    
    curr = [[0.0 for _ in range(8)] for _ in range(8)]
    curr[r][c] = 1.0
    
    for step in range(k):
        next_dp = [[0.0 for _ in range(8)] for _ in range(8)]
        for i in range(8):
            for j in range(8):
                if curr[i][j] > 0:
                    for dx, dy in moves:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < 8 and 0 <= nj < 8:
                            next_dp[ni][nj] += curr[i][j] / 8.0
        curr = next_dp 
    
    total_prob = sum(sum(row) for row in curr)
    return total_prob


if __name__ == "__main__":
    r, c, k = map(int, input().split())  
    print(knight_probability(r, c, k))
