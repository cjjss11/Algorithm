class Solution {
    public int solution(String my_string) {
        int answer = 0;
        String[] alpha = {"1", "2", "3", "4", "5", "6", "7", "8", "9"};
        String[] str_lst = my_string.split("");
        for (int i=0; i<str_lst.length; i++) {
            for (int j=0; j<alpha.length; j++) {
                if (str_lst[i].equals(alpha[j])) {
                    answer += Integer.parseInt(str_lst[i]);
                }
            }
        }
        return answer;
    }
}