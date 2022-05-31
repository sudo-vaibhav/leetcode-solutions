class Solution {
    ArrayList<List<String>> res;
    String s;
    public boolean isPalin(StringBuilder sb){
        int l=0,r=sb.length()-1;
        while(l<r){
            if(sb.charAt(l)!=sb.charAt(r)){
                return false;
            }
            l++;
            r--;
        }
        return true;
    }
    
    public void solve(int index,ArrayList<StringBuilder> path){
        if(index==s.length()){
            var ans = new ArrayList<String>();
            for(var sub:path){
                ans.add(sub.toString());
            }
            res.add(ans);
        }
        else{
            var cur = new StringBuilder();
            for(int i=index;i<s.length();i++){
                cur.append(s.charAt(i));
                if (isPalin(cur)){
                    path.add(cur);
                    solve(i+1,path);
                    path.remove(path.size()-1);
                }
            }
        }
    }
    public List<List<String>> partition(String s) {
        this.s = s;
        res = new ArrayList<List<String>>();
        solve(0,new ArrayList<StringBuilder>());
        
        return res;
    }
}