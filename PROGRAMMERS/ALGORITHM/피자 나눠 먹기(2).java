class Solution {
    public int solution(int n) {
        int answer = 0;
        for (int i=1; i<=6; i++) {
            int num = n * i;
            if (num % 6 == 0) {
                answer = num / 6;
                break;
            }
        }
        return answer;
    }
}