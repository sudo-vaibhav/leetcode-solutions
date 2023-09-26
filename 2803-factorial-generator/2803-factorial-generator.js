/**
 * @param {number} n
 * @yields {number}
 */
function* factorial(n) {
    let cur = 1
    if(n==0) yield 1
    for(var i=1;i<=n;i++){
        cur*=i
        yield cur
    }
};


/**
 * const gen = factorial(2);
 * gen.next().value; // 1
 * gen.next().value; // 2
 */