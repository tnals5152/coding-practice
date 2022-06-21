class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        position_1 = [index for index, v in enumerate(boxes) if v == "1"]#1이 저장되어 있는 인덱스 값들을 리스트에 저장
        result = []
        
        for index in range(len(boxes)):
            result.append(sum([abs(index - v) for v in position_1]))
            
        return result
