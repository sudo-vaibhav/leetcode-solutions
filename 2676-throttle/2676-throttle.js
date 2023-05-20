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
    if (curTime>=nextRun){
        nextRun = curTime+t
        clearTimeout(timeout)
        // if(!timeout){
        fn(...args)
            
        // }
        // timeout = setTimeout(()=>{
        //     fn(...args)
        // },t)
    }
    else{
        if(timeout) clearTimeout(timeout)
        timeout = setTimeout(()=>{
            nextRun = new Date().getTime()+t
            fn(...args)
        },nextRun-curTime)
    }
    // fn(...args)
  }
};

/**
 * const throttled = throttle(console.log, 100);
 * throttled("log"); // logged immediately.
 * throttled("log"); // logged at t=100ms.
 */