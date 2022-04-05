/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */

class Solution {
public:
    int guessNumber(int n) {
        int low= 1,high=n;
        while(low<=high){
            auto m = low + (high-low)/2;
            if(guess(m)==0){
                return m;
            }
            else if(guess(m)==1){
                low=m+1;
            }
            else{
                high = m-1;
            }
            
        }
        
        return -1;
    }
};