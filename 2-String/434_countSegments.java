import static java.lang.System.out;
import java.util.*;
class Solution {
    public int countSegments(String s) {
        int res=0;
        for(int i=0; i<s.length(); i++)
            if(s.charAt(i)!=' ' && (i==0 || s.charAt(i-1)==' '))
                res++;        
        return res;
    }
}

// Time complexity:  O(n)
// Space complexity: O(1)
public class Segments{
    public static void main(String[] args){
        String s = "h h ";
        Solution sol = new Solution();
        int ans = sol.countSegments(s);
        System.out.print(ans);
    }
}