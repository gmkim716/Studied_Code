class Solution {
    public String solution(String my_string) {
        String answer = "";
        char[] charArr = new char[1000];
        for (int i=my_string.length()-1; i>=0; i--) {
            answer += my_string.charAt(i);
        }
        return answer;
    }
}