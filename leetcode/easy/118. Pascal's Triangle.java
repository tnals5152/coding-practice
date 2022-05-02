class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> resultList = new ArrayList<>();
        
        for (int i = 0; i < numRows; i++) {
            List<Integer> row = new ArrayList<>();
            row.add(1);
            if (i != 0) {
                List<Integer> preRow = resultList.get(i - 1);
                for (int index = 0; index < preRow.size() - 1; index++){
                    row.add(preRow.get(index) + preRow.get(index + 1));
                }
                row.add(1);
            }
            resultList.add(row);
        }
        
        return resultList;
    }
}
