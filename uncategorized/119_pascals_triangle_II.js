/**
 * @param {number} rowIndex
 * @return {number[]}
 */
var getRow = function(rowIndex) {

    if(rowIndex === 0) return [1]
    let prev = [1]
    let row = 0

    do {
        row ++
        let curr = [1]

        for(let i=0; i< prev.length -1; i++){
            curr.push(prev[i] + prev[i+1])
        }
        curr.push(1)

        if(row === rowIndex) return curr
        prev = curr

    } while(true)

};