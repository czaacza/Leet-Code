class Solution {
    
    public int rec(int n, int[] nums){
        if (n == 1){
            return 1;
        }
        int i = 1;
        int total = 0;
        
        while (i <= n){
            int left_len = i == 1 ? 1 : i-1;
            int right_len = i == n ? 1 : n - i;
            
            int left_val = -1;
            int right_val = -1;
            
            if (nums[left_len] != -1){
                left_val = nums[left_len];
            } else{
                left_val = rec(left_len, nums);
            }
            
            if (nums[right_len] != -1){
                right_val = nums[right_len];
            } else{
                right_val = rec(right_len, nums);
            }
            
            total += (left_val * right_val);
            i++;
        }
        
        nums[n] = total;
        return total;
    }
    
    public int numTrees(int n) {
        int[] nums = new int[n + 1];
        Arrays.fill(nums, -1);
        
        return rec(n, nums); 
    }
}