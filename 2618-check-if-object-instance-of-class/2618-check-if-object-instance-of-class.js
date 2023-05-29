/**
 * @param {any} obj
 * @param {any} classFunction
 * @return {boolean}
 */
var checkIfInstanceOf = function(obj, classFunction) {
    if (obj===null||obj===undefined||typeof classFunction!=='function') return false;
    let proto = Object.getPrototypeOf(obj)
    
    while (proto!==null){
        if (proto===classFunction.prototype) return true
        proto = Object.getPrototypeOf(proto)
    }
    
    return false;
};

/**
 * checkIfInstanceOf(new Date(), Date); // true
 */