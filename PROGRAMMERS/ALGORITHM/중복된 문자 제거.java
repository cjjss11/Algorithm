import java.util.Arrays;
import java.util.LinkedHashSet;
import java.util.Set;

// 첫 번째 풀이
class Solution {
    public String solution(String my_string) {
        String answer = "";
        String[] str_lst = my_string.split("");
        for (int i=0; i<str_lst.length; i++) {
            for (int j=0; j<i;j++) {
                if (str_lst[i].equals(str_lst[j])){
                    str_lst[i] = "";
                }
            }
        }
        for (int i=0; i<str_lst.length; i++) {
            answer += str_lst[i];
        }
        return answer;
    }
}

// 두 번째 풀이
class Solution {
    public String solution(String my_string) {
        String answer = "";
        String[] str_lst = my_string.split("");
        Set<String> set = new LinkedHashSet<String>(Arrays.asList(str_lst));
        answer = String.join("", set);
        return answer;
    }
}


