/**
 * @param {Function} fn
 * @return {Function<Promise<number>>}
 */
var promisify = function(fn) {
    // console.log(fn.toString())
 	return async function(...args) {
        // console.log(args)
		return new Promise((resolve,reject)=>{
            fn((v,e)=>{
                if (e) {
                   reject(e)
                }
                
                resolve(v)
            },...args)
        })
	}
};

/**
 * const asyncFunc = promisify(callback => callback(42));
 * asyncFunc().then(console.log); // 42
 */