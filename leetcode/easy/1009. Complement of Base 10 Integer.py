class Solution:
    def bitwiseComplement(self, n: int) -> int:
        str_2 = bin(n)[2:]
        str_2 = str_2.replace("1", "2").replace("0", "1").replace("2", "0")
        return int("0b" + str_2, 2)
