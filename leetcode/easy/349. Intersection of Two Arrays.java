import java.util.*;

class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        Map<Integer, Boolean> nums1Map = new HashMap<>();
        Set<Integer> resultSet = new HashSet<>();
        for (int i = 0; i < nums1.length; i++) {
            nums1Map.put(nums1[i], true);
        }
        
        for (int i = 0; i < nums2.length; i++) {
            if (nums1Map.get(nums2[i]) != null) {
                resultSet.add(nums2[i]);
            }
        }
        
        int[] result = new int[resultSet.size()];
        
        Iterator<Integer> iterator = resultSet.iterator();
        
        int index = 0;
        while (iterator.hasNext()) {
            result[index] = iterator.next();
            index++;
        }
        
        return result;
    }
}
