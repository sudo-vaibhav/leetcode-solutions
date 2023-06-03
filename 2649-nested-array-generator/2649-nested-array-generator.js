/**
 * @param {Array} arr
 * @return {Generator}
 */
var inorderTraversal = function*(arr) {
    if (typeof arr==="number") {
        yield arr;
    }
    for(let i=0;i<arr.length;i++){
        const elem = arr[i]
        const traversal = inorderTraversal(elem)
        yield* traversal
         
    }
};

/**
 * const gen = inorderTraversal([1, [2, 3]]);
 * gen.next().value; // 1
 * gen.next().value; // 2
 * gen.next().value; // 3
 */