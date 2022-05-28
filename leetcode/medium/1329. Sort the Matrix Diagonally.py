class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        width = len(mat[0])
        high = len(mat)
        
        for index in range(width):
            get_index_lists, values = self.find_index_values(width, high, index, 0, mat)

            for lists, i in zip(get_index_lists, values):
                column, row = lists
                mat[column][row] = i
                
        for index in range(1, high):
            get_index_lists, values = self.find_index_values(width, high, 0, index, mat)

            for lists, i in zip(get_index_lists, values):
                column, row = lists
                mat[column][row] = i
                
        return mat
            
        
    def find_index_values(self, width: int, high: int, index_w: int, index_h: int, mat: List[List[int]]):
        row = index_w
        column = index_h
        result = []
        values = []
        
        while row < width and column < high:
            result.append((column, row))
            values.append(mat[column][row])
            column += 1
            row += 1

        return result, sorted(values)
        
