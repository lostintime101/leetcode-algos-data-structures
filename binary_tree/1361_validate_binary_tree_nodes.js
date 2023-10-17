/**
 * @param {number} n
 * @param {number[]} leftChild
 * @param {number[]} rightChild
 * @return {boolean}
 */
var validateBinaryTreeNodes = function(n, leftChild, rightChild) {

    let seen = new Array(n).fill(0);

    for(let i=0; i<leftChild.length; i++){
        if(leftChild[i] !== -1) seen[leftChild[i]] ++
        if(rightChild[i] !== -1) seen[rightChild[i]] ++
    }
    // console.log(seen)
    let prev = new Array()

    for(let i=0; i<seen.length; i++){
        if(seen[i] > 1) return false
        if(seen[i] === 0) prev.push(i)
    }

    if(prev.length !== 1) return false
    // console.log(prev)
    seen.fill(0)
    seen[prev[0]] = 1

    while(prev.length > 0) {

        let curr = new Array()

        for(node of prev) {
            if(leftChild[node] !== -1){
                curr.push(leftChild[node])
                seen[leftChild[node]] ++
            }
            if(rightChild[node] !== -1){
                curr.push(rightChild[node])
                seen[rightChild[node]] ++
            }
        }
        prev = curr
    }

    let check = new Array(n).fill(1)
    // console.log(seen, check)
    return JSON.stringify(seen) === JSON.stringify(check);


};