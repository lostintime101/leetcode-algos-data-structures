/**
 * @param {number[]} nums
 * @return {number}
 */
var countNicePairs = function(nums) {

    const MOD = (10**9) + 7
    const seen = {}

    for(let num of nums){
        let rev = parseInt(num.toString().split('').reverse().join(''))
        seen[rev-num] = (seen[rev-num] || 0) +1
    }

    let ans = 0
    for(let v of Object.values(seen)){
        ans += ((v-1) * v) / 2
    }

    return ans % MOD
};