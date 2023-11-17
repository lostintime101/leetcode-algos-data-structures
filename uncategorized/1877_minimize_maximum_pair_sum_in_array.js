/**
 * @param {number[]} nums
 * @return {number}
 */
var minPairSum = function(nums) {

    nums.sort((a,b) => a-b)
    let ans = 0

    for(let i=0; i<nums.length/2; i++){
        ans = Math.max(ans, nums[i] + nums[nums.length - (i+1)])
    }
    return ans
};