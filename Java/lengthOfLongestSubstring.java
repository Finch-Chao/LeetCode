class Solution {
    public int LongestSubstring(String s) {
        int len, pre = 0, max = 0;
        if(s == null || (len = s.length()) == 0) {
        	return 0;
        }
        int[] hash = new int[128];
        int l = 0;
        for(int i = 0; i < len; i++) {
            char c = s.charAt(i);
            if(hash[c] > pre) {
                pre = hash[c];
            }
            l = i - pre + 1;
            hash[c] = i + 1;
            if(l > max){
            	max = l;
            }
        }
        return max;
    }
}