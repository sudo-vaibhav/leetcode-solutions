/**
 * @param {Function} fn
 * @return {Function}
 */
var curry = function(fn) {
    const expected = fn.length;
    let received = [];
    return function curried(...args) {
        received.push(...args)
        if (received.length===expected){
            return fn(...received)
        }
        else{
            return curried
        }
    };
};

/**
 * function sum(a, b) { return a + b; }
 * const csum = curry(sum);
 * csum(1)(2) // 3
 */
