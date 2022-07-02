class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        return list(str(int("".join(map(str,num)))+k))

        # 시간초과
        # return list(str(sum([10 ** (len(num) - index - 1) * n for index, n in enumerate(num)]) + k))