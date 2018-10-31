class Solution(){

    private HashMap<Character, Character> mappings;

    public Solution(){
        this.mappings = new HashMap<Character, Character>();
        this.mappings.put(')', '(');
        this.mappings.put(']', '[');
        this.mappings.put('}', '{');
    }

    public boolean isValid(String s){

        // initialize a stack
        Stack <Character> stack = new Stack<Character>;
        
        for (int i=0; i<s.length(); i++){
            char c = s.charAt(i);
            // if the current character is a closing bracket
            if (this.mappings.containKey(c)){
                char topElement = stack.empty() ? '#' : stack.pop()

                if (topElement != this.mappings.get(c)){
                    return false;
                }
            } else {
                stack.push(c);
            }
        }
        return stack.isEmpty();
    }
}