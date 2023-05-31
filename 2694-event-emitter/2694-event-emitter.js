class EventEmitter {  
  constructor(){
    this.dataStore = {}
  }
  subscribe(event, cb) {
      console.log(this.dataStore)
     this.dataStore[event] = this.dataStore[event]||[]
      this.dataStore[event].push(cb)
    return {
        unsubscribe: () => {
            this.dataStore[event] = this.dataStore[event].filter(c=>c!==cb)
        }
    };
  }

  emit(event, args = []) {

     this.dataStore[event] = this.dataStore[event]||[] 
      const callbacks = this.dataStore[event]
    // console.log(callbacks);
    return callbacks.map(cb=>cb&&cb(...args))
  }
    
}

/**
 * const emitter = new EventEmitter();
 *
 * // Subscribe to the onClick event with onClickCallback
 * function onClickCallback() { return 99 }
 * const sub = emitter.subscribe('onClick', onClickCallback);
 *
 * emitter.emit('onClick'); // [99]
 * sub.unsubscribe(); // undefined
 * emitter.emit('onClick'); // []
 */