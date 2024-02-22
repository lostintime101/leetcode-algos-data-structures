/**
 * @param {number} n
 * @param {number[][]} trust
 * @return {number}
 */
var findJudge = function(n, trust) {

    let trusts = Array(n).fill(0);
    let isTrusted = Array(n).fill(0);

    for(let t of trust){
        trusts[t[0]-1] = 1;
        isTrusted[t[1]-1] += 1;
    }

    for(let i=0; i<n; i++){
        if(trusts[i] === 0 && isTrusted[i] === n-1){
            return i+1;
        }
    }

    return -1;

};