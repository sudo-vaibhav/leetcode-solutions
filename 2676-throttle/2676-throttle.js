/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var throttle = function(fn, t) {
  let nextRun = 0
  let timeout = null
  return function(...args) {
    let curTime = new Date().getTime()
    clearTimeout(timeout)
    if (curTime>=nextRun){
        nextRun = curTime+t
        fn(...args)
    }
    else{
        timeout = setTimeout(()=>{
            nextRun = new Date().getTime()+t
            fn(...args)
        },nextRun-curTime)
    }
  }
};

/**
 * const throttled = throttle(console.log, 100);
 * throttled("log"); // logged immediately.
 * throttled("log"); // logged at t=100ms.
 */