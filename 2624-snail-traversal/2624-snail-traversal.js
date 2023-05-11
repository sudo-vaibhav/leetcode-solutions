/**
 * @param {number} rowsCount
 * @param {number} colsCount
 * @return {Array<Array<number>>}
 */
Array.prototype.snail = function(rc, cc) {
    const prod = rc*cc
    if (this.length!==prod) return []
    let ans = [...Array(rc).fill(0)].map(()=>[...Array(cc).fill(0)])
    let i=0,j=0;
    let dir = true;
    this.forEach(elem=>{
        ans[i][j]=elem
        i+= dir?1:-1;
        if(i==rc){
            i=rc-1;
            dir = false;
            j+=1;
        }
        else if(i==-1){
            dir = true;
            j+=1;
            i=0
        }
        else{
            // i++;
        }
    })
    
    return ans;
}

/**
 * const arr = [1,2,3,4];
 * arr.snail(1,4); // [[1,2,3,4]]
 */