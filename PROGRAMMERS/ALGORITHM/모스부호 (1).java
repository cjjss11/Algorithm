// 첫 번째 방법
class Solution {
    public String solution(String letter) {
        String answer = "";
        String[] morse = {".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};
        char[] alpha = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
        String[] str_letter = letter.split(" ");
        for (int i=0; i<str_letter.length; i++) {
            for (int j=0; j<morse.length; j++) {
                if (str_letter[i].equals(morse[j])) {
                    answer += alpha[j];
                }
            }
        }
        return answer;
    }
}

// 두 번째 방법
class Solution {
    public String solution(String letter) {
        String answer = "";
        String[] morse = {".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};
        String[] str_letter = letter.split(" ");
        for (int i=0; i<str_letter.length; i++) {
            for (int j=0; j<morse.length; j++) {
                if (str_letter[i].equals(morse[j])) {
                    answer += (char)(97+j);
                }
            }
        }
        return answer;
    }
}