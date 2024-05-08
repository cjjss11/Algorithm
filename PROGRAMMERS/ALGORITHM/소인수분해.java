import java.util.ArrayList;
import java.util.Arrays;

class Solution {
    public int[] solution(int n) {
        ArrayList<Integer> lst = new ArrayList<Integer>();
        int i = 2;
        while (i <= n) {
            if (n % i == 0) {
                if (!lst.contains(i)) {  // i가 lst에 없으면
                    lst.add(i);
                }
                n = n / i;
            } else {
                i += 1;
            }
        }
        
        int[] answer = new int[lst.size()];
        for (int j=0; j<lst.size(); j++) {
            answer[j] = lst.get(j);
        }
        Arrays.sort(answer);
        return answer;
    }
}