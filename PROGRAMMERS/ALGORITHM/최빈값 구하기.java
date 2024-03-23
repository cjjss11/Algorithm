class Solution {
    public int solution(int[] array) {
        int answer = 0;
        int[] index = new int[array.length+1]; 
        int max = Integer.MIN_VALUE; 
        
        for(int i=0; i<array.length; i++){
           index[array[i]]++;
        }
        
        for(int i=0; i<index.length; i++){
            if( max<index[i] ){ 
                max = index[i];
                answer = i ;  
            } else if(max == index[i]) { 
                answer = -1;
            }
        }
        
        return answer;
    }
}