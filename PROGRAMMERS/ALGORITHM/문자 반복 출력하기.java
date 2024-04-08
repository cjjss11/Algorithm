class Solution {
    public String solution(String my_string, int n) {
        String answer = "";
        String[] my_str = my_string.split("");
        for (int i=0; i<my_str.length; i++) {
            for (int j=0; j<n; j++) {
                answer += my_str[i];
            }
        }
        return answer;
    }
}