import java.util.*;
class Solution {
    public List<Integer> majorityElement(int[] nums) {
        int n = nums.length / 3;
        
        Map<Integer, Integer> numCountMap = new HashMap<>();
        List<Integer> resultList = new ArrayList<>();
        
        for (int i = 0; i < nums.length; i++) {
            numCountMap.put(nums[i], numCountMap.getOrDefault(nums[i], 0) + 1);
        }
        
        for (Integer key : numCountMap.keySet()) {
            if (numCountMap.get(key) > n) {
                resultList.add(key);
            }
        }
        return resultList;
    }
}
