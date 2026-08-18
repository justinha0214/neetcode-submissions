class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> numbers = new HashSet<>();

        for (int num : nums) {
            if (numbers.contains(num)) {
                return true;
            }
            else {
                numbers.add(num);
            }
        }
        return false;
    }
}