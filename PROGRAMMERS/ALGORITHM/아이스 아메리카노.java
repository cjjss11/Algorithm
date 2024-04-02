class Solution {
    public int[] solution(int money) {
        int coffee = 0;
        int charge = 0;

        coffee = money / 5500;
        charge = money - (coffee * 5500);
        
        int[] answer = {coffee, charge};
            
        return answer;
    }
}