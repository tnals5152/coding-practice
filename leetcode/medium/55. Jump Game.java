class Solution {
    public boolean canJump(int[] nums) {
        int length = nums.length;
        boolean[] checkArray = new boolean[length];
        
        for (int i = 0; i < nums.length; i++) {
            if (i != 0 && !checkArray[i]) {
                return false;
            }
            
            int jumpIndex = nums[i] + i;
            for (int index = i + 1; index <= jumpIndex && index < length; index++) {
                    checkArray[index] = true;
            }
        }
        return true;
    }
}
