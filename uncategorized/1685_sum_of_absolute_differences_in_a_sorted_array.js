/**
 * @param {number[]} nums
 * @return {number[]}
 */
var getSumAbsoluteDifferences = function(nums) {

    const ans = new Array(nums.length).fill(0)
    let forwardBase = nums.reduce((a,b) => a+b)
    let backwardBase = 0

    for(let i in nums){

        const forward = forwardBase - (nums[i] * (nums.length-i))
        const backward = (nums[i]* i) - backwardBase

        forwardBase -= nums[i]
        backwardBase += nums[i]

        ans[i] = Math.abs(forward +backward)
    }

    return ans

};