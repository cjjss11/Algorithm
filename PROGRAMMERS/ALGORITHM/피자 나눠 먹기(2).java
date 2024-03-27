class Solution {
    public int solution(int n) {
        int answer = 1000;
        int pizza = 0;
        for (int i=1; i<=6; i++) {
            int num = n * i;
            if (num % 6 == 0) {
                pizza = num / 6;
                if (pizza < answer) {
                    answer = pizza;
                }
            }
        }
        return answer;
    }
}