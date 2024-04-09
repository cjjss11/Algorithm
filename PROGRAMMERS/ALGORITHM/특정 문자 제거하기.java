// 첫 번째 방법

class Solution {
    public String solution(String my_string, String letter) {
        String answer = "";
        String[] my_str = my_string.split("");
        for (int i=0; i<my_str.length; i++) {
            if (!my_str[i].equals(letter)) {
                answer += my_str[i];
            }
        }
        return answer;
    }
}

// 두 번째 방법

class Solution {
    public String solution(String my_string, String letter) {
        String answer = "";
        answer = my_string.replace(letter, "");
        return answer;
    }
}