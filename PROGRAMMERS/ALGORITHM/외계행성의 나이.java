class Solution {
    public String solution(int age) {
        String answer = "";
        char[] alpha = {'a','b','c','d','e','f','g','h','i','j'};
        while (age > 0) {
            int num = age % 10;
            answer = alpha[num] + answer;
            age = age / 10;
        }
        return answer;
    }
}