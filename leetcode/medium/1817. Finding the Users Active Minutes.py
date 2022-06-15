class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        result = [0] * k
        
        logs_dict = dict()
        
        for log in logs:
            if logs_dict.get(log[0]) is None:
                logs_dict[log[0]] = set()
            logs_dict[log[0]].add(log[1])
            
        for key, item in logs_dict.items():
            result[len(item) - 1] += 1
        
        return result
        
