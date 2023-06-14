class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        height = len(mat)
        width = len(mat[0])
        pos = []

        for i in range(height):
            for j in range(width):
                if mat[i][j] == 0:
                    pos.append((i,j))
                else:
                    mat[i][j] = "#"
        
        for row, column in pos:
            for dx, dy in (1,0), (-1,0), (0,1), (0,-1):
                nr = row + dx
                nc = column + dy
                if 0 <= nr < height and 0 <= nc < width and mat[nr][nc] == "#":
                    mat[nr][nc] = mat[row][column] + 1
                    pos.append((nr,nc))
        
        return mat

        

