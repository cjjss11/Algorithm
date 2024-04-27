class Solution {
    public int solution(int[] numbers, int k) {
        int answer = 0;
        int num = 1; // 몇 번째인지 확인
        int idx = 0;
        while (num <= k) {
            num ++;
            idx += 2;
            if (idx > numbers.length-1) {
                idx = idx - numbers.length;
            }
            if (num == k) {
                answer = numbers[idx];
            }
        }
        return answer;
    }
}