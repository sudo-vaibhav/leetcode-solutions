import java.util.*;
class Solution {
    public boolean isValid(String s) {
         Stack<Character> st = new Stack<Character>();
        HashMap<Character,Character> mapping = new HashMap<Character,Character>();
        mapping.put('(',')');
        mapping.put('{','}');
        mapping.put('[',']');
        // while string has characters
        try{
        // keep pushing all opening brackets
            for(int x=0;x<s.length();x++){
            char i = s.charAt(x);
            if(mapping.containsKey(i)){
                st.push(i);
            }
            else{
                char topElement = st.pop();
                if(mapping.get(topElement)!=i){
                    return false;
                }
            }
        }
            // keep doing this

            // in the end stack should become empty
            
            // otherwise give false
            return st.isEmpty();
        }
        catch(Exception e){
            return false;
        }
    }
}