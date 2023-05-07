/**
 * @param {Function} fn
 * @param {number} t milliseconds
 * @return {Function}
 */
var debounce = function(fn, t) {
    let timeout = undefined;
    return function(...args) {
        // if(!timeout){
        clearTimeout(timeout)
        timeout = setTimeout(()=>{
                timeout=undefined
                fn(...args)
            },t)
        // }
    }
};

/**
 * const log = debounce(console.log, 100);
 * log('Hello'); // cancelled
 * log('Hello'); // cancelled
 * log('Hello'); // Logged at t=100ms
 */