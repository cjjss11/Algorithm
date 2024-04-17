import java.util.Arrays;

class Solution {
    public int[] solution(int[] emergency) {
        int[] answer = new int[emergency.length];
        int[] reverse = Arrays.copyOf(emergency, emergency.length);;
        Arrays.sort(reverse);
        for (int i=0; i<reverse.length / 2; i++) {
            int temp = reverse[i];
            reverse[i] = reverse[reverse.length - i - 1];
            reverse[reverse.length - i - 1] = temp;
        }
        for (int i=0; i<reverse.length; i++) {
            for (int j=0; j<emergency.length; j++) {
                if (reverse[i] == emergency[j]) {
                    answer[j] = i+1; 
                }
            }
        }
        return answer;
    }
}