/**
 * @param {number[]} nums
 * @return {number}
 */
var minOperations = function(nums) {

    let ans = 0
    let freq = {}

    for(let num of nums){
        freq[num] = (freq[num] || 0) + 1
    }

    for(let v of Object.values(freq)){
        if(v === 1){
            return -1
        }
        let curr = v % 3
        ans += parseInt(v/3)
        if(curr !== 0){
            ans += 1
        }
    }

    return ans

};