import java.util.Arrays;

class Solution {
    public int[] solution(String my_string) {
        String result = "";
        String[] str_lst = my_string.split("");
        String[] number = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"};
        for (int i=0; i<str_lst.length; i++) {
            for (int j=0; j<number.length; j++) {
                if (str_lst[i].equals(number[j])) {
                    result += str_lst[i];
                }
            }
        }
        String[] result_lst = result.split("");
        int[] answer = new int[result_lst.length];
        for (int i=0; i<result_lst.length; i++) {
            answer[i] = Integer.parseInt(result_lst[i]);
        }
        Arrays.sort(answer);
        return answer;
    }
}