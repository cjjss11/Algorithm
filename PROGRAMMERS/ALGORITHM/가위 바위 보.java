class Solution {
    public String solution(String rsp) {
        String answer = "";
        String[] rsp_lst = rsp.split("");
        for (int i=0; i<rsp_lst.length; i++) {
            if (rsp_lst[i].equals("2")) {
                answer += "0";
            } else if (rsp_lst[i].equals("0")) {
                answer += "5";
            } else if (rsp_lst[i].equals("5")) {
                answer += "2";
            }
        }
        return answer;
    }
}