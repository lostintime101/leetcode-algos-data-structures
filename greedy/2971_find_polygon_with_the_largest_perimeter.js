/**
 * @param {number[]} nums
 * @return {number}
 */
var largestPerimeter = function(nums) {

    let ans = -1;
    nums = nums.sort((a,b) => a-b);

    let count = nums[0] + nums[1];

    for(let i=2; i<nums.length; i++){
        if(nums[i] < count){
            count += nums[i];
            ans = Math.max(count, ans);
        } else {
            count += nums[i];
        }
    }

    return ans;

};