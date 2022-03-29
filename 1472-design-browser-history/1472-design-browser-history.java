class BrowserHistory {
//     b contains all previous page and current page on top
    
    //  f contains all next pages from current page (wont have current page itself)
    Stack<String> f,b;
    public BrowserHistory(String homepage) {
        f = new Stack<>();
        b = new Stack<>();
        b.push(homepage);
    }
    
    public void visit(String url) {
        b.push(url);
        f = new Stack<String>();
    }
    
    public String back(int steps) {
        while(steps>0 && b.size()>1){
            // var t = s.peek();
            
            f.push(b.pop());
            steps--;
        }
        return b.peek();
    }
    
    public String forward(int steps) {
        while(!f.empty() && steps>0){
            steps--;
            b.push(f.pop());
        }
        
        return b.peek();
    }
}

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * BrowserHistory obj = new BrowserHistory(homepage);
 * obj.visit(url);
 * String param_2 = obj.back(steps);
 * String param_3 = obj.forward(steps);
 */