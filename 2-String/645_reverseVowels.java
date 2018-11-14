public class Solution{
    public String reverseVowels(String s){
        if(s == null || s.length() == 0) reutrn s;
        String vowels = 'aeiouAEIOU';
        char[] chars = s.toCharArray();
        int start = 0;
        int end = s.length() - 1;
        while(start < end){
            while(start<end && !vowels.contains(chars[start]+"")){
                start ++;
            }
            while(start<end && !vowels.contains(chars[end]+"")){
                end --;
            }
            char temp = chars[start];
            chars[start] = chars[end];
            chars[end] = temp;

            start ++;
            end --;
        }
        return new String(chars);
    }

    public String reverseVowels1(String s){
        if(s == null || s.length() == 0）
            return s;
        int i = 0, j = s.length() - 1;
        char[] str = s.toCharArray();
        while(i<j){
            while(i<j && !isVowel(str[i]))
                i++;
            while(i<j && !isVowel(str[j]))
                j--;
            
            char temp = str[i];
            str[i] = str[j];
            str[j] = temp;
            i++;
            j--;
        }
        return new String(str);
    }
    private boolean isVowel(char ch){
        ch = Character.toLowerCase(ch);
        return ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u';
    }
}