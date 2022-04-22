from itertools import combinations
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = 10 ** 4

        for i1, num in enumerate(nums[:-2]):
            i2 = i1 + 1#i1보다 큰 인덱스부터 시작
            i3 = len(nums) - 1#마지막 인덱스부터 시작
            
            while i2 < i3:
                total = nums[i1] + nums[i2] + nums[i3]
                
                if total == target:
                    return total
                
                if abs(total - target) < abs(closest - target):#현재 차이가 더 작으면 closest 값 변경
                    closest = total
                
                if total - target > 0:#total이 0보다 크면 제일 큰 값의 인덱스인 i3의 인덱스를 줄여줌
                    i3 -= 1
                else:#total이 0보다 작으면 더 작은 값인  i2의 인덱스를 더해줌
                    i2 += 1
                
                
                
        return closest
        
        
        
        
        
        
        
        
        
        
#         시간초과
#         combination = list(combinations(nums, 3))
#         closest = 10 ** 4
        
#         for a, b, c in combination:
#             if abs(target - closest) > abs(target - (a + b + c)):
#                 closest = a + b + c
#         return closest
        
        
