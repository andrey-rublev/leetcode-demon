class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lr = 0
        lc = 0
        rr = len(matrix)
        rc = len(matrix[0])
        while lr<rr or (lr==rr and lc<rc):
            r = (lr+rr)//2
            c = (lc+rc)//2
            if matrix[r][c] < target:
                lr = r
                lc = c + 1
            elif matrix[r][c] > target:
                rr = r
                rc = c - 1
            elif matrix[r][c] == target:
                return True
        return False
