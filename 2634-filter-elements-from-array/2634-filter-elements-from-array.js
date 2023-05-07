/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    const ans = []
    arr.forEach((...args)=>{
        if(fn(...args)){
            ans.push(args[0])
        }
    })
    return ans
};