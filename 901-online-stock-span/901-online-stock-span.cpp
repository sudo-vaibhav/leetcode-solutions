class StockSpanner {
public:
    stack<pair<int,int>> st;
    StockSpanner() {
        // s = stack<pair<int,int>>();
    }
    
    int next(int price) {
        int span = 1;
        while(st.empty() == false and st.top().first <= price) {
            span += st.top().second;
            st.pop();
        }
        
        st.push({price, span});
        return span;
        
    }
};

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner* obj = new StockSpanner();
 * int param_1 = obj->next(price);
 */