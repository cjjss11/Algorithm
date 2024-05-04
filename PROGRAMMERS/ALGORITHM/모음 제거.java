class Solution {
    public String solution(String my_string) {
        String answer = "";
        String[] alpha = {"a", "e", "i", "o", "u"};
        String[] str_myString = my_string.split("");
        for (int i=0; i<str_myString.length; i++) {
            int flag = 0;
            for (int j=0; j<alpha.length; j++) {
                if (str_myString[i].equals(alpha[j])) {
                    flag = 1;
                }
            }
            if (flag == 0) {
                answer += str_myString[i];
            }
        }
        return answer;
    }
}