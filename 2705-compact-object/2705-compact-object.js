/**
 * @param {Object} obj
 * @return {Object}
 */
var compactObject = function(obj) {
    if(typeof obj==="object" && obj!==null){
        const ans = Array.isArray(obj) ? []: {}
        Object.keys(obj).forEach(k=>{
            const val = compactObject(obj[k])
            if(Boolean(val)){
                if(Array.isArray(ans)){
                    ans.push(val)
                }
                else
                ans[k]=val    
            }
        })
        return ans
    }
    else{
        return obj
    }
};