/**
 * @return {Object}
 */
var createInfiniteObject = function() {
    const proxy = new Proxy({},{
        get: (target,prop)=>{
            return ()=>prop
        }
    })
    return proxy
};

/**
 * const obj = createInfiniteObject();
 * obj['abc123'](); // "abc123"
 */