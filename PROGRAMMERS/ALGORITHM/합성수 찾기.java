class Solution {
    public int solution(int n) {
        int answer = 0;
        for (int i=1; i<=n; i++) {
            double num = Math.sqrt(i);
            int cnt = 0;
            for (int j=1; j<=(int)num; j++) {
                if (i % j == 0) {
                    if (j == i/j) {
                        cnt += 1;
                    } else {
                        cnt += 2;
                    }
                }
            }
            if (cnt >= 3) {
                answer ++;
            }
        }
        return answer;
    }
}