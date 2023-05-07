/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    const ans = []
    arr.forEach((elem,idx)=>ans.push(fn(elem,idx)))
    return ans
};