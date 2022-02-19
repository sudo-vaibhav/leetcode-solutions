class Solution {
public:
    string countAndSay(int n) {
        string num = "1";
        
        while(n-->1){
            string current = num+" ";
            char prev = current[0];
            int i=0;
            int count=0;
            string temp = "";
            while(i<current.size()){
                if(current[i]==prev){
                    count++;
                }
                else{
                    temp += to_string(count);
                    temp += prev;
                    count=1;
                }
                prev = current[i];
                i++;
                
            }
            num = temp;
        }
        
        return num;
    }
};