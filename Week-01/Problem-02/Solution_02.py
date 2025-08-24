# BFS Approach :-

from collections import deque

def floodFillBFS(image, sr, sc, newColor):
    rows, cols = len(image), len(image[0])
    originalColor = image[sr][sc]
    
    if originalColor == newColor:
        return image
    
    queue = deque([(sr, sc)])
    
    while queue:
        r, c = queue.popleft()
        if image[r][c] == originalColor:
            image[r][c] = newColor
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == originalColor:
                    queue.append((nr, nc))
    
    return image

