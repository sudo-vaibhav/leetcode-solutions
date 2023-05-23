/**
 * @param {Array} arr
 * @return {Matrix}
 */
var jsonToMatrix = function(arr) {
    const keys = new Set()
    const isObject = (val)=>typeof val=="object" && val!=null
    const getKeys = (row,prev="")=>{
        if(typeof row==="string"|typeof row==="boolean"||typeof row==="number"||row===null){
            keys.add(prev)
        }
        else{
            Object.keys(row).forEach(k=>{
                getKeys(row[k],(prev.length?(prev+"."):prev)+k)
            })
        }
    }
    arr.forEach(row=>{
        getKeys(row)
    })
    
    const sortedKeys = [...keys].sort()
    
    const ans = [
        [...sortedKeys]
    ]
    
    const getVal = (row,key)=>{
        
        const segs = key.split(".")
        for(let i=0;i<segs.length;i++){
            if(!isObject(row) || !(segs[i] in row )){
                return undefined
            }
            else{
                row = row[segs[i]]
            }
        }
        if(isObject(row)) return undefined
        return row
    }
    arr.forEach(row=>{
       const temp = []
       // console.log(row)
       sortedKeys.forEach(key=>{
           const val = getVal(row,key)
           // console.log(row,key,val)
            if((typeof val==="object"&&val!==null)||val===undefined){
            temp.push("")
           }
           else{
               temp.push(val)
           }
       })
        ans.push(temp)
    })
    
    return ans
    
    
};