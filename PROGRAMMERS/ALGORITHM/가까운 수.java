class Solution {
    public int solution(int[] array, int n) {
        int answer = 0;
        int num = 0;
        int minn = 100;
        
        for (int i=0; i<array.length; i++) {
            num = Math.abs(array[i] - n);
            if (num < minn) {
                minn = num;
                answer = array[i];
            } else if (num == minn) {
                if (answer > array[i]) {
                    answer = array[i];
                }
            }
        }
        return answer;
    }
}