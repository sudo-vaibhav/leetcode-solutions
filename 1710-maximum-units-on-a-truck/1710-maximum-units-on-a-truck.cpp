class Solution {
public:
    
    
    // [[5,10],[2,5],[4,7],[3,9]]                           10
    int maximumUnits(vector<vector<int>>& boxTypes, int truckSize) {
            // the number of units , give me descending order
        
        auto comp = [](pair<int,int> p1, pair<int,int> p2){
            return p1.first < p2.first;
        };
        priority_queue<pair<int,int>, vector<pair<int, int>>, decltype(comp)> pq(comp); // max heap by default 
        // first -> unit count , second -> frequency/count 
        
        for(auto boxType:boxTypes){
                        // 5
            // for(int i=0;i<boxType[0];i++){
            pq.push({boxType[1],boxType[0]}); // 10,10,10,10,10
            // }
        }
        
        int units  = 0;  // will have our units added on truck so far
       // 4                     4 elements
        while(truckSize>0 && !pq.empty()){ // as long as truck size is positive
            auto boxType = pq.top(); // 10
            auto unitCount = boxType.first;
            auto boxCount = boxType.second;
            
            // truckSize -= min(truckSize,truckSize-boxCount);
            int boxesUsed;
            if(truckSize>boxCount){
                boxesUsed = boxCount;
            }
            else{
                boxesUsed = truckSize;
            }
            
            pq.pop(); // remove
            units += boxesUsed * unitCount; // increase units 
            truckSize-= boxesUsed; // decrease box capacity
        }
        
        return units; // return ans
    }
};