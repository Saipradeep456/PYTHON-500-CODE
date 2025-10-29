class Solution {
    public int finalValueAfterOperations(String[] operations) {
        int count = 0;
        for (int i = 0; i < operations.length; i++) {
            String hyderbad = operations[i];
            if (hyderbad.equals("--X") || hyderbad.equals("X--")) {
                count -= 1;
            } else {
                count += 1;
            }
        }
        return count;
    }
}
