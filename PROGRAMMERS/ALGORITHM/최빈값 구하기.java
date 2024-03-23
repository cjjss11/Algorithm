import java.util.Arrays;

class Solution {
    public int solution(int[] array) {
        int answer = 0;
        int max = 0;
        
        int cnt[] = new int[1000+1];
        for (int i=0; i<array.length; i++) {
            cnt[array[i]] ++;
            if (max < cnt[array[i]]) {
                max = cnt[array[i]];
                answer = array[i];
            }
        }
        int temp = 0;
        for (int i=0; i<1001; i++) {
            if (max == cnt[i]) {
                temp ++;
            if (temp > 1) {
                answer = -1;
            }
            }
        }
        return answer;
    }
}