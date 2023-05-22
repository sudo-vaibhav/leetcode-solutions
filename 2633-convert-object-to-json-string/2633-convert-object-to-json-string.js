/**
 * @param {any} object
 * @return {string}
 */
function jsonStringify (obj) {
    if (["number","boolean"].includes(typeof obj)) return `${obj}`
    else if(typeof obj==="string") return `"${obj}"`
    else if (obj===null) return "null"
    else if (Array.isArray(obj)) return `[${obj.map(v=>jsonStringify(v)).join(",")}]`
    
    const keys = Object.keys(obj)
    const reps = keys.map(k=>{
        
        const v = obj[k]
        // if(typeof v==="object"){
            return `"${k}":${jsonStringify(v)}`
        // }
        // else{
        //     return `"${k}":${v}`
        // }
    })
    
    return `{${reps.join(",")}}`
    
};