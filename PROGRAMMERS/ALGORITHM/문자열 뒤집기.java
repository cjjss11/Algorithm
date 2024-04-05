class Solution {
    public String solution(String my_string) {
        String answer = "";
        String [] my_str = my_string.split("");
        for (int i=my_str.length-1; i>=0; i--) {
            answer += my_str[i];
        }
        return answer;
    }
}