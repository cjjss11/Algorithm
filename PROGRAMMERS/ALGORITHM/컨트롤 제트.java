class Solution {
    public int solution(String s) {
        int answer = 0;
        String[] s_lst = s.split(" ");
        for (int i=0; i<s_lst.length; i++) {
            if (!s_lst[i].equals("Z")) {
                int num = Integer.parseInt(s_lst[i]);
                answer += num;
            } else {
                int num = Integer.parseInt(s_lst[i-1]);
                answer -= num;
            }
        }
        return answer;
    }
}