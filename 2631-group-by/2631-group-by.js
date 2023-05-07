/**
 * @param {Function} fn
 * @return {Array}
 */
Array.prototype.groupBy = function(fn) {
    const groups = {}
    this.forEach(val=>{
        const k = fn(val)
        if(k in groups){
            groups[k].push(val)
        }
        else{
            groups[k]=[val]
        }
    })
    return groups
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */