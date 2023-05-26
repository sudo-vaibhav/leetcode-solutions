/**
 * @param {any[]} arr
 * @param {number} depth
 * @return {any[]}
 */
var flat = function (arr, n) {
    let ans = arr
    
    while(n--){
        let temp = []
        // console.log(n,ans)
        ans.forEach(elem=>{
           if(typeof elem==="number"){
               temp.push(elem)
           } 
            else{
                temp.push(...elem)
            }
        })
        ans=temp
    }
    
    return ans
};