class Solution {
    public int fib(int n) {
        int first_num = 0;
        int second_num = 1;
        
        for (int i=0; i < n; i++){
            int added = first_num + second_num;
            first_num = second_num;
            second_num = added;
        }
        
        return first_num;
    }
}