/**
 * @param {string} s
 * @return {number}
 */
var countHomogenous = function(s) {

    const MOD = 10**9 + 7
    let ret = 0, prev = "A", count = 1

    for(l of s){
        if(l === prev) count ++
        else count = 1

        prev = l
        ret += count

    }

    return ret % MOD

};