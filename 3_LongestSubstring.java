// Brute Force 检查 s 的所有子串
// 时间复杂度 O(n3)，空间复杂度 O(min(n, m))
public class Solution1{
    public int lengthOfLongestSubstring(String s){
        int n = s.length();
        int ans = 0;
        for (int i = 0; i < n; i++)
            for (int j = i + 1; j <= n; j++)
                if (allUnique(s, i, j)) ans = Math.max(ans, j - i);
        return ans;
    }
    public bollean allUnique(String s, int start, int end){
        Set<Character> set = new HashSet<>();
        for(int i = start; i < end; i++){
            Character ch = s.charAt(i);
            if(set.contains(ch)) return false;
            set.add(ch);
        }
        return true;
    }
}

// Sliding Window 左闭右开，检查下一个字符是否在当前子串中
// 使用 HashSet 作为滑动窗口，从 O(n2) 降到O(1)
// time complexity O(2n) = O(n)
public class Solution{
    public int lengthOfLongestSubstring(String s){
        int n = s.length();
        Set<Character> set = new HashSet<>();
        int ans = 0, i = 0, j = 0;
        while (i < n && j < n){
            // try to extend the range[i, j]
            if (!set.contains(s.charAt(j))){
                set.add(s.charAt(j++));
                ans = Math.max(ans, j - i)
            }
            else{
                set.remove(s.charAt(i++));
            }
        }
        return ans;
    }
}



s = 'abckkddd'
sol = Solution()
res = sol.lengthOfLongestSubstring(s)
system.out.printlin(res)





















