class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 and len(trust) == 0:
            return n
        
        trust_dict = dict()
        """
        trust_dict = {
            1: [3, 4], #1번이 믿는 사람 리스트
        }
        """
        my_dict = dict()
        """
        my_dict = {
            3: [1, 2, 4], #3번을 믿는 사람 리스트
        }
        """
        
        for person in trust:
            if not trust_dict.get(person[0]):
                trust_dict[person[0]] = []
            trust_dict[person[0]].append(person[1])
            
            if not my_dict.get(person[1]):
                my_dict[person[1]] = []
            my_dict[person[1]].append(person[0])
            
        for judge_num in [key for key, value in my_dict.items() if len(value) == n - 1]:
            if not trust_dict.get(judge_num):
                return judge_num
        return -1
