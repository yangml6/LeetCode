class Solution {
    public int compress(char[] chars){
        int indexAns = 0, index = 0;
        while(index < chars.length){
            char currentChar = chars[index];
            int count = 0;
            while(index < chars.length && chars[index] == currentChar){
                index++;
                count++;
            }
            chars[indexAns++] = currentChar;
            if(count != 1)
                for(char c : Integer.toString(count).toCharArray())
                    chars[indexAns++] = c;
        }
        return indexAns;
    }

    public int compress2(char[] chars){
        int start = 0;
        for (int end = 0, count = 0; end < chars.length; end++){
            count++;
            if(end == chars.length-1 || chars[end]!=chars[end+1]){
                // have found a difference or at the end of array
                // then update character at start pointer
                chars[start] = chars[end];
                start++;
                if(count != 1){
                    // Copy over the character count to the array
                    char[] arr = String.valueOf(count).toCharArray();
                    for(int i=0; i<arr.length;i++, start++)
                        chars[start] = arr[i];
                }
                // Reset the counter
                count = 0;
            }
        }   
        return start;
    }
}

public class compress{
    public static void main(String[] args){
        char chars[] ={ 'a', 'b', 'b' };
        Solution sol = new Solution();
        int ans = sol.compress2(chars);
        System.out.println(ans);
    }
}