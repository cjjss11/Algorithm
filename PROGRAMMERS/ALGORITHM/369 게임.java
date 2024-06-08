class Solution {
    public int solution(int order) {
        int answer = 0;
        String order_str = Integer.toString(order);
        String[] order_lst = order_str.split("");
        for (int i=0; i<order_lst.length; i++) {
            if (order_lst[i].equals("3") || order_lst[i].equals("6") || order_lst[i].equals("9")) {
                answer += 1;
            }
        }
        return answer;
    }
}