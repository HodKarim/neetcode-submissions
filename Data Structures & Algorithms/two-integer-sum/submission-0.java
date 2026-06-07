class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        for (int i=0; i<nums.length ; i++){
            for (int j = i+1 ; j<nums.length ; j++) {
                int check = nums[i] + nums[j];
                if ( check == target) {
                    int [] result = {i,j};
                    return result;
                }
            }
        } return nums;
    }    
}

//given array of ints (nums) and one integer (target)
//return the indices i and j s.t the numbers in those indices
//add up to the target AND i is not equal to j

