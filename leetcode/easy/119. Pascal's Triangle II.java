class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> beforeRow = new ArrayList<>();
        beforeRow.add(1);
        
        for (int row = 1; row <= rowIndex; row++) {
            List<Integer> nowRow = new ArrayList<>();
            nowRow.add(1);
            
            for (int i = 0; i < beforeRow.size() - 1; i++) {
                nowRow.add(beforeRow.get(i) + beforeRow.get(i + 1));
            }
            nowRow.add(1);
            beforeRow = nowRow;
        }
        
        return beforeRow;
    }
}
