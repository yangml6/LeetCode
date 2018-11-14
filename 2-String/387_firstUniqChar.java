public class Solution{
    public int firstUniqChar(String s){
        int freq [ ] = new int[26];
        for (int i = 0; i < s.length(); i++)
            freq [s.charAt(i) - 'a'] ++;
        for (int i = 0; i < s.length(); i++)
            if(freq[s.charAt(i) - 'a'] == 1)
                return i;
        return -1;
    }

    public int firstUniqChar2(String s){
        if(s == null || s.length() == 0) return -1;
        int len = s.length();
        if(len == 1) return 0;
        char[] cc = s.toCharArray();
        int slow = 0, fast = 1;
        int[] count = new int[256];
        count[cc[slow]]++;
        while(fast < len){
            count[cc[fast]]++;
            while(slow < len && count[cc[slow]] > 1) slow++;
            if(slow >= len) return -1;
            if(count[cc[slow]] == 0){
                count[cc[slow]]++;
                fast = slow;
            }
            fast++;
        }
        return slow;
    }
}
