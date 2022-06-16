class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        result_list = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        sum_dict = dict()
        
        for i, v in enumerate(mat):
            for j, v2 in enumerate(v):
                sum_ = 0
                
                r_min= max(0, i - k)
                r_max = min(len(mat), i + k + 1)
                c_min = max(0, j - k)
                c_max = min(len(v), j + k + 1)
                
                if sum_dict.get(f"{r_min}-{r_max}-{c_min}-{c_max}"):
                    result_list[i][j] = sum_dict[f"{r_min}-{r_max}-{c_min}-{c_max}"]
                    continue
                
                for r in range(r_min, r_max):
                    for c in range(c_min, c_max):
                        sum_ += mat[r][c]
                result_list[i][j] = sum_
                sum_dict[f"{r_min}-{r_max}-{c_min}-{c_max}"] = sum_
        
        return result_list
