/**
 * @param {Array} arr
 * @return {Generator}
 */
var inorderTraversal = function*(arr) {
    if (typeof arr==="number") {
            // console.log(elem)
            yield arr;
        }
    for(let i=0;i<arr.length;i++){
        const elem = arr[i]
        // console.log(arr,elem)
        
        // else{
        const traversal = inorderTraversal(elem)
            yield* traversal
            // while(true){
            //     const val = traversal.next().value;
            //     if (val!==undefined){
            //         yield val
            //     }
            //     else{
            //         break
            //     }
            // }
        // }
         
    }
};

/**
 * const gen = inorderTraversal([1, [2, 3]]);
 * gen.next().value; // 1
 * gen.next().value; // 2
 * gen.next().value; // 3
 */