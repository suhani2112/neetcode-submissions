// import java.util.*;
class Solution {
    public List<String> generateParenthesis(int n) {
        List<String>result = new ArrayList<>();
        backtracks("",0,0,n,result);
        return result;
        }
    private void backtracks(String s, int open, int close , int n , List<String> result){
        if(s.length()== 2*n){
            result.add(s);
            return;
        }
        if(open < n){
                backtracks(s + "(" , open+1,close, n, result);
            }
        if(close<open){
            backtracks(s+")", open , close+1, n, result);
            }
        }
}
