
const isObj = (obj)=>{
    return typeof obj === "object" && obj!==null
}
/**
 * @param {object} obj1
 * @param {object} obj2
 * @return {object}
 */

function solve(obj1,obj2){
    const ans = {}
    
    if (!isObj(obj1)||!(isObj(obj2))) return obj1===obj2?{}: [obj1,obj2]
    if(Array.isArray(obj1)!==Array.isArray(obj2)) return [obj1,obj2]
    
    const keys1 = new Set(Object.keys(obj1))
    const keys2 = new Set(Object.keys(obj2))
    
    Array.from(keys1).forEach(k=>{
        if(keys2.has(k)){
            const temp = objDiff(obj1[k],obj2[k])
            // console.log(temp,k,obj1,obj2)
            if (Object.keys(temp).length!==0){
                ans[k]=temp
            }
        }
    })
    // if(Object.keys(ans).length===0) return undefined
    
    return ans
}
function objDiff(obj1, obj2) {
    return solve(obj1,obj2)
    
};