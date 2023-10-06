/**
 * @param {number} n
 * @return {number}
 */
var integerBreak = function(n) {

    // edge cases
    if(n === 2) return 1
    if(n === 3) return 2

    let ans = 1
    while(n > 2){
        ans *= 3
        n -= 3
    }
    if(n === 1) return (ans / 3) * 4
    if(n === 2) return ans * 2

    return ans

};