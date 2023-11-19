/**
 * @param {number[]} nums
 * @return {number}
 */
var reductionOperations = function(nums) {

    nums.sort((a,b) => b - a)

    let ans = 0

    for(let i=1; i<nums.length; i++){
        if(nums[i] !== nums[i-1]) ans += i
    }

    return ans

};