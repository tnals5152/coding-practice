import java.util.*;
class Solution {
    public int majorityElement(int[] nums) {
        
        HashMap<Integer, Integer> count = new HashMap<>();//숫자 : 나타난 갯수
        double numsLength = nums.length / 2.0;
        
        for (int i = 0; i < nums.length; i++) {
            Integer total = count.get(nums[i]);
            if (total == null) {
                total = 0;
            }
            total++;
            if (total >= numsLength) {
                return nums[i];
            }
            count.put(nums[i], total);
        }
        return 0;
        
        
        
        
//         첫번째 방법
//         HashMap<Integer, Integer> count = new HashMap<>();//숫자 : 나타난 갯수
        
//         for (int i = 0; i < nums.length; i++) {
//             count.put(nums[i], count.getOrDefault(nums[i], 0) + 1);
//         }

//         for (Integer key: count.keySet()) {
//             if (count.get(key) >= nums.length / 2.0) {
//                 return key;
//             }
//         }
//         return 1;
    }
}
