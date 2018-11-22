// Time complexity:  O(n)
// Space complexity: O(1)
class Solution {
    public int countSegment(String s) {
        int res=0;
        for(int i=0; i<s.length(); i++)
            if(s.charAt(i)!=' ' && (i==0 || s.charAt(i-1)==' '))
                res++;        
        // System.out.println(res);        
        return res;
    }
}

public class countSegments{
    public static void main(String[] args){
        String s = "h h j";
        Solution sol = new Solution();
        int ans = sol.countSegment(s);
        System.out.println(ans);
    }
}
