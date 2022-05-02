import java.util.*;
class Solution {
    public int[] sortArrayByParity(int[] A) {
        int evenCount = 0;
        for(int i:A){
            if(i%2==0) evenCount++;
        }
        int front = 0;
        int back = A.length-1;
        while(front!=evenCount){
            if(A[front]%2==1){
                while(A[back]%2!=0){
                    back--;
                }
                A[front] = A[back]+A[front];
                A[back] = A[front] - A[back];
                A[front] = A[front] - A[back];
                
                back--;
            }
            front++;
        }
        return A;
    }
}