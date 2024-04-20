class Solution {
    public int solution(int n) {
        int answer = 0;
        double result = Math.sqrt(n);
        for (int i=1; i<=(int)result; i++) {
            if (n % i == 0) {
                if (i == n/i) {
                    answer += 1;
                } else{
                    answer += 2;
                }
            }
        }
        return answer;
    }
}