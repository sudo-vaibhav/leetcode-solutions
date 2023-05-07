/**
 * @return {Generator<number>}
 */
var fibGenerator = function*() {
    let x=0;
    let y=1;
    yield 0;
    yield 1;
    while(true){
        let z = x+y;
        x = y;
        y = z;
        yield z
    }
};

/**
 * const gen = fibGenerator();
 * gen.next().value; // 0
 * gen.next().value; // 1
 */