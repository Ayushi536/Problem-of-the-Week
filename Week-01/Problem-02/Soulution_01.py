# DFS Approach :- 

def floodFillDFS(image, sr, sc, newColor):
    """
    Perform flood fill on a 2D image using DFS.

    Args:
    image (list[list[str]]): 2D matrix representing the image.
    sr (int): Starting row index.
    sc (int): Starting column index.
    newColor (str): New color to fill.

    Returns:
    list[list[str]]: Updated image after flood fill.
    """
    rows, cols = len(image), len(image[0])
    originalColor = image[sr][sc]

    if originalColor == newColor:
        return image  # No need to fill if the color is same

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if image[r][c] != originalColor:
            return
        
        image[r][c] = newColor
        
        # Move in 4 directions
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    dfs(sr, sc)
    return image

# Example usage
image = [
    ['B', 'B', 'W'],
    ['W', 'W', 'W'],
    ['W', 'W', 'W'],
    ['B', 'B', 'B']
]
sr, sc = 2, 2
newColor = 'G'

updated_image = floodFillDFS(image, sr, sc, newColor)
for row in updated_image:
    print(row)
